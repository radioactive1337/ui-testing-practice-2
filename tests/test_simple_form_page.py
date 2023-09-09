import pytest
from pages.SimpleFormPage import SimpleFormPage


@pytest.mark.parametrize("message, val1, val2", [("hello world", 44, 55)])
@pytest.mark.selected
def test_simpleformpage(driver, message, val1, val2):
    page = SimpleFormPage(driver, 'simple-form-demo')
    page.open()
    page.fill_inp_message(message)
    page.fil_full_form_sum(val1, val2)
    assert page.verify_message_result(message), "message result isn't correct"
    assert page.verify_sum_result(val1, val2), "sum result isn't correct"
