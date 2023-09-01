import pytest
from pages.simple_form_page import SimpleFormPage


@pytest.mark.parametrize("message, val1, val2", [("hello world", 44, 55)])
def test_simpleformpage(driver, message, val1, val2):
    page = SimpleFormPage(driver, 'https://www.lambdatest.com/selenium-playground/simple-form-demo')
    page.open()
    page.fill_inp_message(message)
    page.fil_full_form_sum(val1, val2)
    assert page.verify_message_res(message)
    assert page.verify_sum_res(val1, val2)
