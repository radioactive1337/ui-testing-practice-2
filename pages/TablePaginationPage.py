from .BasePage import BasePage
from selenium.webdriver.common.by import By


class TablePaginationPageLocators:
    NEXT_PAGE = (By.XPATH, "//span[text()=' > ']")
    ROW_NUMBERS = (By.XPATH, "//select[@class='form-control']")
    PAGE_1 = (By.XPATH, "//li[@data-page='1']")
    PAGE_2 = (By.XPATH, "//li[@data-page='2']")
    PAGE_3 = (By.XPATH, "//li[@data-page='3']")


class TablePaginationPage(BasePage):
    def select_rows_num(self, row):
        self.select_value(TablePaginationPageLocators.ROW_NUMBERS, row)

    def next_page(self):
        self.click_element(TablePaginationPageLocators.NEXT_PAGE)

    def page_number_is_correct(self, locator):
        return self.get_element_attribute(locator, "class") == "active"
