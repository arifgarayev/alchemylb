import subprocess

from appium.webdriver.appium_service import AppiumService

class Server:

    def __init__(self):
        self.appium_service = AppiumService()
        self.server_process = None




    def start_server(self, port, udid):
        self.server_process = self.appium_service.start(args=['--port', f'{port}',
                                    '--session-override', '-bp', '400',
                                    '--default-capabilities', "{\"udid\":\"%s\"}" % udid
                                    ], stdout=subprocess.PIPE, timeout_ms=120000)
        return self



    # terminate appium server, via API
    def stop_server(self):

        if self.server_process and self.appium_service:

            self.appium_service.stop()
