from .base_page import BasePage
from selenium.webdriver.common.by import By


class GoogleLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.XPATH, '//div[@class="FPdoLc lJ9FBc"]//input[@value="Мне повезёт!"]')


class Google(BasePage):

    def button_click(self):
        button = self.find_element(GoogleLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        button.click()
