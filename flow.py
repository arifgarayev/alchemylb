import time

from src.services.g_sheet import GoogleSheet
from src.services.server import Server
from src.services.driver import Device
from src.services.database.repository.repo import Repo


from src.views.root import RootView
from src.views.modal import Modal
from src.views.search_modal import SearchModalView
from src.views.slider_modal import SliderModal



from src.utils.cli_commands import Commands
from src.utils.common import Utils
from src.utils.helper import Helper

import os, sys


os.path.dirname(__file__)

class Flow:

    _current_km = None

    def __init__(self,
                 driver_dependecy : dict,
                 routes : dict,
                 service_acc_token_fp : str):



        self.udid = driver_dependecy['desired_caps']['udid']
        self.port = driver_dependecy['host']['port']
        self.pkg_name = driver_dependecy['android_pkg_name']

        self.routes = routes




        Commands.is_device_online(self.udid)


        Commands.sigkill_appium_process(self.port)\
            .release_port_adb(self.udid).kill_app(self.udid,
                                                  self.pkg_name).\
            clean_appium_pkgs(self.udid)

        time.sleep(7)



        #TODO enable in production
        self.g_sheet = GoogleSheet(service_acc_token_fp,
                                   driver_dependecy['gsheet_id'],
                                   driver_dependecy['sheet_name'])

        self.server = Server().\
            start_server(self.port,
                self.udid)



        # before selenium remote connection

        self.driver = Device(driver_dependecy['desired_caps'],
                             driver_dependecy['host']).\
            get_driver()


        self.db_conn = Repo(driver_dependecy['db_path'])

        print()




    def start(self):

        root_view, \
            modal_view, \
            search_modal_view, \
            slider_modal_view = self.phase_one()

        time.sleep(5)




        # TODO enable in production code
        while True:
            try:
                self.iteration(root_view, search_modal_view, modal_view, slider_modal_view)

            except Exception as e:

                print(e, '\n', '\n')
                print(f"Last checked km is - {self._current_km}")


                self.server.stop_server()


                # Add validation for current_km instance (float)
                if self._current_km:

                    self.db_conn.append_active_log(self._current_km)

                Commands.kill_app(self.udid, self.pkg_name). \
                    sigkill_appium_process(self.port) \
                    .release_port_adb(self.udid). \
                    clean_appium_pkgs(self.udid)


                sys.exit(1)






    def iteration(self, root_view,
                  search_modal_view,
                  modal_view,
                  slider_modal_view):

        last_checked_km = self.db_conn.get_last_log()[0][0]

        _reduced_routes = self._reduce_routes_hash(last_checked_km)


        for km_range in _reduced_routes:

            _routes = _reduced_routes[km_range]

            self._current_km = float(km_range)


            for origin, destination in _routes.items():
                economy, comfort, comfort_plus = self.phase_two(root_view). \
                    phase_three(search_modal_view, origin). \
                    phase_four(search_modal_view, modal_view, root_view, destination). \
                    phase_five(modal_view).phase_six(slider_modal_view)





                print("Economy --- ETA ", *economy)
                print("Comfort --- ETA ", *comfort)
                print("Comfort+ --- ETA ", *comfort_plus)
                print('------------------------------------')

                # TODO enable in production
                self.g_sheet.add_data_new(
                                          Utils.get_date_today(),
                                          Utils.get_time_now(),
                                          km_range,
                                          *Helper.filter_output(economy),
                                          *Helper.filter_output(comfort),
                                          *Helper.filter_output(comfort_plus)
                                          )

                self.phase_seven(modal_view)

        if self._current_km:
            self.db_conn.append_active_log(self._current_km)






    def phase_one(self):

        instances = []

        Commands.launch_app(self.udid, self.pkg_name)

        for cls in (RootView, Modal, SearchModalView, SliderModal):

            instances.append(cls(self.driver))

        return instances



    # def filter_output(self, *args):
    #
    #     eco, com, comp = args
    #
    #     checker = lambda _tuple : ('Busy', 'Busy') if 'from' in _tuple else _tuple
    #
    #     return checker(eco), checker(com), checker(comp)
    #



    def phase_two(self, root_view : RootView):

        root_view.click_to_gps()

        time.sleep(5)

        root_view.click_to_input()

        time.sleep(3)

        return self


    def phase_three(self, search_modal_view : SearchModalView, origin):

        search_modal_view.select_origin_route(origin)

        time.sleep(5)

        return self



    def phase_four(self, search_modal_view : SearchModalView, modal_obj, root_view_obj, destination):

        search_modal_view.select_destination_route(destination, modal_obj, root_view_obj)

        time.sleep(5)


        return self



    def phase_five(self, modal_view : Modal):

        modal_view.destroy_bottom_sheet()

        time.sleep(3)


        modal_view.reset_session_view()

        time.sleep(3)

        modal_view.expand_slider()

        time.sleep(3)

        return self


    def phase_six(self, slider_modal_view : SliderModal):


        return (
            (slider_modal_view.get_price("Economy"),
                 slider_modal_view.get_eta()),
            (slider_modal_view.get_price("Comfort"),
             slider_modal_view.get_eta()),
            (slider_modal_view.get_price("Comfort+"),
             slider_modal_view.get_eta())
                )


    def phase_seven(self, modal_view : Modal):

        modal_view.go_back()

        time.sleep(3)

        modal_view.reset_modal_view()

        time.sleep(5.5)



    def _reduce_routes_hash(self, last_checked_km):

        _routes = self.routes.copy()

        km_keys = list(
            map(
        lambda x: str(x),
        list(self.routes.keys())
            )
        )

        if str(last_checked_km) in km_keys:

            if float(last_checked_km) != float(km_keys[-1]):

                index = km_keys.index(str(last_checked_km)) + 1

                for i in range(index):
                    del _routes[km_keys[i]]


        return _routes

