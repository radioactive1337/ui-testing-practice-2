from .BasePage import BasePage
from selenium.webdriver.common.by import By


class CheckboxPageLocators:
    # section 1
    CHECKBOX_1 = (By.XPATH, "//label[text()='Click on check box']")
    CHECKBOX_1_INFO = (By.XPATH, "//div[@id='txtAge']")
    # section 2
    DISABLED_CHECKBOX_2 = (By.XPATH, "//div[@class='pb-10']//label[text()='Option 3']")
    DISABLED_CHECKBOX_3 = (By.XPATH, "//div[@class='pb-10']//label[text()='Option 4']")
    # section 3
    BUTTON_CHECK_ALL = (By.XPATH, "//input[@type='button']")


class CheckboxPage(BasePage):
    def select_checkbox(self, locator):
        self.click_element(locator)

    def single_checkbox_is_checked(self):
        return self.get_element_attribute(CheckboxPageLocators.CHECKBOX_1_INFO, "style") == ""

    def double_checkboxes_is_disabled(self):
        return (self.get_element_attribute(CheckboxPageLocators.DISABLED_CHECKBOX_2, "disabled") is None and
                self.get_element_attribute(CheckboxPageLocators.DISABLED_CHECKBOX_2, "disabled") is None)

    def quad_checkboxes_is_checked(self):
        return self.get_element_attribute(CheckboxPageLocators.BUTTON_CHECK_ALL, "value") == "Uncheck All"
