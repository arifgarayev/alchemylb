from src.views.base import BaseView
from src.resources.locators import RootLocators


class RootView(BaseView):
    def __init__(self, driver):
        super().__init__(driver)

    def click_to_gps(self):
        return self.click(RootLocators.gps_circle)

    def click_to_input(self):
        return self.click(RootLocators.where_to)
