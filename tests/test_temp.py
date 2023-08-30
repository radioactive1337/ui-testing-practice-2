import pytest

from pages.temp_page import Google
import time


@pytest.mark.q
def test1(driver):
    yandex = Google(driver, 'https://www.google.com/')
    yandex.open()
    yandex.button_click()
    time.sleep(5)
