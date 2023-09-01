from .base_page import BasePage

from selenium.webdriver.common.by import By


class SimpleFormLocators:
    MESSAGE_INPUT = (By.XPATH, "//input[@id='user-message']")
    MESSAGE_INPUT_BUTTON = (By.XPATH, "//button[@id='showInput']")
    MESSAGE_RESULT = (By.XPATH, "//p[@id='message']")
    FIRST_VALUE_INPUT = (By.XPATH, "//input[@id='sum1']")
    SECOND_VALUE_INPUT = (By.XPATH, "//input[@id='sum2']")
    SUM_VALUES_BUTTON = (By.XPATH, '//button[contains(text(), "Get Sum")]')
    SUM_RESULT = (By.XPATH, "//p[@id='addmessage']")


class SimpleFormPage(BasePage):
    def send_text_for_message_inp(self, message):
        self.get_element(SimpleFormLocators.MESSAGE_INPUT).send_keys(f"{message}")
        self.get_element(SimpleFormLocators.MESSAGE_INPUT_BUTTON).click()

    def send_values_for_sum(self, val1, val2):
        self.get_element(SimpleFormLocators.FIRST_VALUE_INPUT).send_keys(val1)
        self.get_element(SimpleFormLocators.SECOND_VALUE_INPUT).send_keys(val2)
        self.get_element(SimpleFormLocators.SUM_VALUES_BUTTON).click()

    def get_message_res(self):
        return self.get_element(SimpleFormLocators.MESSAGE_RESULT).text

    def get_sum_res(self):
        return self.get_element(SimpleFormLocators.SUM_RESULT).text
