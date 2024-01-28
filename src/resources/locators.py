"""All type of locators are simple str type, and supportive for XPATH"""


class RootLocators:
    gps_circle = '//android.widget.Button[@content-desc="Detect my location"]'
    where_to = '//android.widget.TextView[@resource-id = "ru.yandex.taxi:id/action_component_title"]'
    hamburger_menu = (
        '//android.widget.ImageView[@resource-id="ru.yandex.taxi:id/hamburger"]'
    )


class SearchModalLocators:
    clear_input = '//android.widget.Button[@content-desc="Clear text box"]'

    origin_top = '//android.widget.FrameLayout[@resource-id="ru.yandex.taxi:id/source_address_input"]'

    origin_text_top = (
        '//android.widget.FrameLayout[@resource-id="ru.yandex.taxi:id/source_address_input"]'
        '/android.widget.LinearLayout/android.widget.FrameLayout[@resource-id="ru.yandex.taxi:id/address_select_input"]'
        '/android.view.ViewGroup/android.widget.LinearLayout[@resource-id="ru.yandex.taxi:id/component_input_center"]'
        '/android.widget.LinearLayout/android.widget.EditText[@resource-id="ru.yandex.taxi:id/component_list_item_input"]'
    )

    destination_bottom = '//android.widget.FrameLayout[@resource-id="ru.yandex.taxi:id/destination_address_input"]'

    destination_text_bottom = (
        '//android.widget.FrameLayout[@resource-id="ru.yandex.taxi:id/destination_address_input"]'
        '/android.widget.LinearLayout/android.widget.FrameLayout[@resource-id="ru.yandex.taxi:id/address_select_input"]'
        '/android.view.ViewGroup/android.widget.LinearLayout[@resource-id="ru.yandex.taxi:id/component_input_center"]'
        '/android.widget.LinearLayout/android.widget.EditText[@resource-id="ru.yandex.taxi:id/component_list_item_input"]'
    )

    # wait until
    # first suggested route - Hard Coded
    suggested_route = '(//android.widget.Button/android.widget.LinearLayout[@resource-id = "ru.yandex.taxi:id/center"])[1]'

    where_to_search_modal = "//android.widget.EditText[@text = 'Where to?']"


class ModalLocators:
    back_circle_button = '//android.widget.Button[@content-desc="Back"]'

    modal_destination_input = '//android.widget.Button[@resource-id="ru.yandex.taxi:id/component_destination_address"]'

    # check if selected (if last session active)
    economy_class = (
        '//android.widget.Button[contains(@content-desc, "Economy service class")]'
    )
    comfort_class = (
        '//android.widget.Button[contains(@content-desc, "Comfort service class")]'
    )
    comfort_plus_class = (
        '//android.widget.Button[contains(@content-desc, "Comfort+ service class")]'
    )

    bottom_sheet = '//android.widget.FrameLayout[@resource-id="ru.yandex.taxi:id/slideable_modal_view_bottom_sheet"]'

    icon = (
        bottom_sheet
        + '/android.widget.FrameLayout[@resource-id="ru.yandex.taxi:id/slideable_modal_view_card_content_container"]/android.widget.LinearLayout[@resource-id="ru.yandex.taxi:id/content"]/android.widget.LinearLayout/android.widget.Button[@resource-id="ru.yandex.taxi:id/yourself"]'
    )


class SliderModalLocators(ModalLocators):
    # example txt = 2 min
    eta = '//android.widget.TextView[@resource-id="ru.yandex.taxi:id/solid_tariff_page_eta"]'
    price = '//android.widget.TextView[@resource-id = "ru.yandex.taxi:id/solid_tariff_page_price"]'
