from .BasePage import BasePage
from selenium.webdriver.common.by import By


class ProgressBarPageLocators:
    BUTTON_DIALOG_2 = (By.XPATH, "//button[contains(text(),'2 sec')]")
    BUTTON_DIALOG_3 = (By.XPATH, "//button[contains(text(),'3 sec')]")
    BUTTON_DIALOG_5 = (By.XPATH, "//button[contains(text(),'5 sec')]")
    DIALOG = (By.XPATH, "//div[@class='modal fade show']")


class ProgressBarPage(BasePage):
    pass
