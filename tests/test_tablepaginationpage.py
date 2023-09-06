import pytest
from pages.TablePaginationPage import TablePaginationPageLocators
from pages.TablePaginationPage import TablePaginationPage


def test_tablepagination(driver):
    page = TablePaginationPage(driver, "table-pagination-demo")
    page.open()
    assert page.page_number_is_correct(TablePaginationPageLocators.PAGE_1)
    page.select_rows_num("10")
    page.next_page()
    assert page.page_number_is_correct(TablePaginationPageLocators.PAGE_2)
    page.next_page()
    assert page.page_number_is_correct(TablePaginationPageLocators.PAGE_3)
