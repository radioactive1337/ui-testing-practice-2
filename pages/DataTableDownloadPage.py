import os

from .BasePage import BasePage
from selenium.webdriver.common.by import By


class DataTableDownloadPageLocators:
    COPY_BUTTON = (By.XPATH, "//a[contains(@class,'buttons-copy')]")
    CSV_BUTTON = (By.XPATH, "//a[contains(@class,'buttons-csv')]")
    EXCEL_BUTTON = (By.XPATH, "//a[contains(@class,'buttons-excel')]")
    PDF_BUTTON = (By.XPATH, "//a[contains(@class,'buttons-pdf')]")
    PRINT_BUTTON = (By.XPATH, "//a[contains(@class,'buttons-print')]")
    COPY_INFO = (By.XPATH, "//div[@class='dt-button-info']")


class DataTableDownloadPage(BasePage):
    def copy_table(self):
        self.click_element(DataTableDownloadPageLocators.COPY_BUTTON)

    def csv_download(self):
        self.click_element(DataTableDownloadPageLocators.CSV_BUTTON)

    def xlsx_download(self):
        self.click_element(DataTableDownloadPageLocators.EXCEL_BUTTON)

    def pdf_download(self):
        self.click_element(DataTableDownloadPageLocators.PDF_BUTTON)

    def open_and_switch_print_version(self):
        self.click_element(DataTableDownloadPageLocators.PRINT_BUTTON)
        self.switch_to_new_window()

    def table_is_copied(self):
        return self.verify_element_present(DataTableDownloadPageLocators.COPY_INFO)

    def print_version_is_existed(self):
        return self.get_url() == "about:blank"

    def pdf_is_dowloaded(self):
        return os.path.isfile("C:\\Users\\radioactive\\Downloads\\Selenium Grid Online  Run Selenium Test On Cloud.pdf")

    def xlsx_is_dowloaded(self):
        return os.path.isfile(
            "C:\\Users\\radioactive\\Downloads\\Selenium Grid Online  Run Selenium Test On Cloud.xlsx")

    def csv_is_dowloaded(self):
        return os.path.isfile("C:\\Users\\radioactive\\Downloads\\Selenium Grid Online  Run Selenium Test On Cloud.csv")
