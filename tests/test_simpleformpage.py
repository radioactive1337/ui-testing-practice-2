import pytest
import time
from pages.simple_form_page import SimpleFormPage


@pytest.mark.parametrize("message, val1, val2", [("hello world", 44, 55)])
@pytest.mark.latest
def test_simpleformpage(driver, message, val1, val2):
    page = SimpleFormPage(driver, 'https://www.lambdatest.com/selenium-playground/simple-form-demo')
    page.open()
    page.send_text_for_message_inp(message)
    page.send_values_for_sum(val1, val2)
    assert page.get_message_res == message
    assert page.get_sum_res == f"{val1 + val2}"
