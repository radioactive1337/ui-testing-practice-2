from .BasePage import BasePage
from selenium.webdriver.common.by import By


class AlertBoxPageLocators:
    ALERT_BUTTON = (By.XPATH, "//p[text()='JavaScript Alerts']/button")
    CONFIRM_BUTTON = (By.XPATH, "//p[text()='Confirm box:']/button")
    PROMPT_BUTTON = (By.XPATH, "//p[text()='Prompt box:']/button")


class AlertBoxPage(BasePage):
    def show_alert_box(self):
        self.click_element(AlertBoxPageLocators.ALERT_BUTTON)

    def show_confirm_box(self):
        self.click_element(AlertBoxPageLocators.CONFIRM_BUTTON)

    def show_prompt_box(self):
        self.click_element(AlertBoxPageLocators.PROMPT_BUTTON)

    def get_alert_hint(self):
        alert = self.driver.switch_to.alert
        return alert.text

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def enter_text_alert(self, text: str):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
