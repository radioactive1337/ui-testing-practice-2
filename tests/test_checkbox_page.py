from pages.CheckboxPage import CheckboxPageLocators
from pages.CheckboxPage import CheckboxPage


def test_checkboxpage(driver):
    page = CheckboxPage(driver, "checkbox-demo")
    page.open()
    page.select_checkbox(CheckboxPageLocators.CHECKBOX_1)
    page.click_element(CheckboxPageLocators.BUTTON_CHECK_ALL)
    assert page.single_checkbox_is_checked()
    assert page.double_checkboxes_is_disabled()
    assert page.quad_checkboxes_is_checked()
