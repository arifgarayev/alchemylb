from selenium import webdriver
from selenium.webdriver import ActionChains


class Device:
    def __init__(self, desired_caps: dict, host):
        self.device_uuid = desired_caps.get("udid")
        self.driver = webdriver.Remote(
            host["host_url"], desired_capabilities=desired_caps
        )

        self.action_chains = ActionChains(self.driver)

    def get_driver(self):
        return self.driver
