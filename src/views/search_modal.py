import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from src.views.base import BaseView
from src.resources.locators import SearchModalLocators, ModalLocators, RootLocators


class SearchModalView(BaseView):
    def __init__(self, driver):
        super().__init__(driver)

    def select_origin_route(self, origin):
        self.click(SearchModalLocators.origin_top).click(
            SearchModalLocators.clear_input
        ).send_text(SearchModalLocators.origin_text_top, origin)

        time.sleep(5)

        try:
            self.click(SearchModalLocators.suggested_route)

            time.sleep(7)

        except (TimeoutException, NoSuchElementException):
            pass

        return self

    # views.modal.Modal object must be initialized in order to run this method
    # it has dependencies
    def select_destination_route(self, destination, modal_obj, root_view_obj):
        """
        Multiple objects for multiple app states, so we pass objects,
        cus we are not sure in which state our app currently is.
        :param destination:
        :param modal_obj:
        :param root_view_obj:
        :return:
        """

        # 2 states for destination route - 1st one is for the blank new app session
        # 2nd is already existing session

        # session 1.
        # when app states is prompting destination input i.e. when destination input exists

        # check is_promting?
        def select():
            self.send_text(SearchModalLocators.destination_text_bottom, destination)

            time.sleep(5)

            return self.click(SearchModalLocators.suggested_route)

        # if self.check_app_state_view(SearchModalLocators.destination_bottom):
        #     # is promting -> 1st state
        #     select()
        #
        #     time.sleep(7)
        #

        if self.check_app_state_view(RootLocators.where_to):
            root_view_obj.click_to_input()

            time.sleep(4)

        elif self.check_app_state_view(ModalLocators.modal_destination_input):
            modal_obj._click_to_destination(ModalLocators.modal_destination_input)

            self.click(SearchModalLocators.clear_input)

        select()

        time.sleep(7)

        return self
