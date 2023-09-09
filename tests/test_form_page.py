import pytest
from pages.FormPage import FormPage


@pytest.mark.parametrize("name, email, passw, company, website, country, city, addr1, addr2, state, zipcode",
                         [("python", "golefi9207@lukaat.com", "pass", "company51", "https://example.com", "AU",
                           "Sydney", "address1", "address2", "state123", "1337")])
def test_formpage(driver, name, email, passw, company, website, country, city, addr1, addr2, state, zipcode):
    page = FormPage(driver, "input-form-demo")
    page.open()
    page.fill_full_form(name, email, passw, company, website, country, city, addr1, addr2, state, zipcode)
    assert page.form_is_submited(), "form isn't correct"
