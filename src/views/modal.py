from src.views.base import BaseView
from src.resources.locators import ModalLocators, SliderModalLocators


class Modal(BaseView):
    def __init__(self, driver):
        super().__init__(driver)

    # for internal usage
    def _click_to_destination(self, locator):
        return self.click(locator)

    def reset_session_view(self):
        if not self.is_selected(ModalLocators.economy_class):
            return self.click(ModalLocators.economy_class)
        return self

    def expand_slider(self):
        self.click(ModalLocators.economy_class)

        self.wait_to_be_visible(SliderModalLocators.price)

    def destroy_bottom_sheet(self):
        if self.check_app_state_view(ModalLocators.bottom_sheet):
            self.click(ModalLocators.icon)

    def reset_modal_view(self):
        return self.click(ModalLocators.back_circle_button)
