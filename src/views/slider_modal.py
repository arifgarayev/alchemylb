from src.views.base import BaseView
from src.resources.locators import ModalLocators, SliderModalLocators


class SliderModal(BaseView):
    def __init__(self, driver):
        super().__init__(driver)

    def get_price(self, category_name):
        if category_name == "Economy":
            # double check

            if not self.is_selected(SliderModalLocators.economy_class):
                self.click(SliderModalLocators.economy_class)

        elif category_name == "Comfort":
            if not self.is_selected(SliderModalLocators.comfort_class):
                self.click(SliderModalLocators.comfort_class)

        elif category_name == "Comfort+":
            if not self.is_selected(SliderModalLocators.comfort_plus_class):
                self.click(SliderModalLocators.comfort_plus_class)

        return (
            self.get_text(SliderModalLocators.price)
            .replace("\u202f", "")
            .replace("₾", "")
        )

    def get_eta(self):
        return self.get_text(SliderModalLocators.eta).replace(" min", "")

    def reset_slider_modal_view(self):
        return self.go_back()
