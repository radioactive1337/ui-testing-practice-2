import pytest
from pages.ProgressBarPage import ProgressBarPage
from pages.ProgressBarPage import ProgressBarPageLocators


def test_progressbarpage(driver):
    page = ProgressBarPage(driver, "bootstrap-progress-bar-dialog-demo")
    page.open()
    # button1
    page.click_element(ProgressBarPageLocators.BUTTON_DIALOG_2)
    assert page.verify_element_present(ProgressBarPageLocators.DIALOG) == True
    page.wait(2)
    assert page.verify_element_present(ProgressBarPageLocators.DIALOG, 1) == False
    # button2
    page.click_element(ProgressBarPageLocators.BUTTON_DIALOG_3)
    assert page.verify_element_present(ProgressBarPageLocators.DIALOG, ) == True
    page.wait(3)
    assert page.verify_element_present(ProgressBarPageLocators.DIALOG, 1) == False
    # button3
    page.click_element(ProgressBarPageLocators.BUTTON_DIALOG_5)
    assert page.verify_element_present(ProgressBarPageLocators.DIALOG) == True
    page.wait(5)
    assert page.verify_element_present(ProgressBarPageLocators.DIALOG, 1) == False
