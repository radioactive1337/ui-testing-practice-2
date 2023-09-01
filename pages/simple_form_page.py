from .base_page import BasePage

from selenium.webdriver.common.by import By


class SimpleFormPageLocators:
    MESSAGE_INPUT = (By.XPATH, "//input[@id='user-message']")
    MESSAGE_INPUT_BUTTON = (By.XPATH, "//button[@id='showInput']")
    MESSAGE_RESULT = (By.XPATH, "//p[@id='message']")
    FIRST_VALUE_INPUT = (By.XPATH, "//input[@id='sum1']")
    SECOND_VALUE_INPUT = (By.XPATH, "//input[@id='sum2']")
    SUM_VALUES_BUTTON = (By.XPATH, '//button[contains(text(), "Get Sum")]')
    SUM_RESULT = (By.XPATH, "//p[@id='addmessage']")


class SimpleFormPage(BasePage):
    def fill_inp_message(self, message):
        self.get_element(SimpleFormPageLocators.MESSAGE_INPUT).send_keys(f"{message}")
        self.get_element(SimpleFormPageLocators.MESSAGE_INPUT_BUTTON).click()

    def fill_first_inp_sum(self, val1):
        self.get_element(SimpleFormPageLocators.FIRST_VALUE_INPUT).send_keys(val1)

    def fill_second_inp_sum(self, val2):
        self.get_element(SimpleFormPageLocators.SECOND_VALUE_INPUT).send_keys(val2)

    def fil_full_form_sum(self, val1, val2):
        self.fill_first_inp_sum(val1)
        self.fill_second_inp_sum(val2)
        self.click_element(SimpleFormPageLocators.SUM_VALUES_BUTTON)

    def verify_message_res(self, message):
        return self.get_element(SimpleFormPageLocators.MESSAGE_RESULT).text == message

    def verify_sum_res(self, val1, val2):
        return self.get_element(SimpleFormPageLocators.SUM_RESULT).text == f"{val1 + val2}"
