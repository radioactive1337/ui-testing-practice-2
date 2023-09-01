from .base_page import BasePage
from selenium.webdriver.common.by import By


class FormLocators:
    NAME_INPUT = (By.XPATH, "//input[@id='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='inputEmail4']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='inputPassword4']")
    COMPANY_INPUT = (By.XPATH, "//input[@id='company']")
    WEBSITE_INPUT = (By.XPATH, "//input[@id='websitename']")
    COUNTRY_INPUT = (By.XPATH, "//select[@name='country']")
    CITY_INPUT = (By.XPATH, "//input[@id='inputCity']")
    ADDRESS1_INPUT = (By.XPATH, "//input[@id='inputAddress1']")
    ADDRESS2_INPUT = (By.XPATH, "//input[@id='inputAddress2']")
    STATE_INPUT = (By.XPATH, "//input[@id='inputState']")
    ZIPCODE_INPUT = (By.XPATH, "//input[@id='inputZip']")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Submit')]")
    SUBMIT_RES = (By.XPATH, "//p[@class='success-msg hidden']")


class FormPage(BasePage):
    def fill_inp_name(self, name):
        self.input_text(FormLocators.NAME_INPUT, name)

    def fill_inp_email(self, email):
        self.input_text(FormLocators.EMAIL_INPUT, email)

    def fill_inp_pass(self, passw):
        self.input_text(FormLocators.PASSWORD_INPUT, passw)

    def fill_inp_company(self, company):
        self.input_text(FormLocators.COMPANY_INPUT, company)

    def fill_inp_website(self, website):
        self.input_text(FormLocators.WEBSITE_INPUT, website)

    def fill_inp_country(self, country):
        self.select_value(FormLocators.COUNTRY_INPUT, country)

    def fill_inp_city(self, city):
        self.input_text(FormLocators.CITY_INPUT, city)

    def fill_inp_addr1(self, addr1):
        self.input_text(FormLocators.ADDRESS1_INPUT, addr1)

    def fill_inp_addr2(self, addr2):
        self.input_text(FormLocators.ADDRESS2_INPUT, addr2)

    def fill_inp_state(self, state):
        self.input_text(FormLocators.STATE_INPUT, state)

    def fill_inp_zip(self, zipcode):
        self.input_text(FormLocators.ZIPCODE_INPUT, zipcode)

    def submit_form(self):
        self.click_element(FormLocators.SUBMIT_BUTTON)

    def fill_full_form(self, name, email, passw, company, website, country, city, addr1, addr2, state, zipcode):
        self.fill_inp_name(name)
        self.fill_inp_email(email)
        self.fill_inp_pass(passw)
        self.fill_inp_company(company)
        self.fill_inp_website(website)
        self.fill_inp_country(country)
        self.fill_inp_city(city)
        self.fill_inp_addr1(addr1)
        self.fill_inp_addr2(addr2)
        self.fill_inp_state(state)
        self.fill_inp_zip(zipcode)
        self.submit_form()

    def form_is_submited(self):
        return "display" in self.get_element_attribute(FormLocators.SUBMIT_RES, "style")
