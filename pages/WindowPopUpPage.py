from .BasePage import BasePage
from selenium.webdriver.common.by import By


class WindowPopupPageLocators:
    TWITTER_BUTTON = (By.XPATH, '//a[contains(text(),"  Follow On Twitter ")]')
    FACEBOOK_BUTTON = (By.XPATH, '//a[contains(text(),"  Like us On Facebook ")]')
    LINKEDIN_BUTTON = (By.XPATH, '//a[contains(text(),"  Follow us On Linkedin ")]')


class WindowPopupPage(BasePage):
    def open_twitter_window(self):
        self.click_element(WindowPopupPageLocators.TWITTER_BUTTON)
        self.wait_for_page_to_load()

    def open_facebook_window(self):
        self.click_element(WindowPopupPageLocators.FACEBOOK_BUTTON)
        self.wait_for_page_to_load()

    def open_linkedin_window(self):
        self.click_element(WindowPopupPageLocators.LINKEDIN_BUTTON)
        self.wait_for_page_to_load()
