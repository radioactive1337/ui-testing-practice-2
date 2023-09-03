from .BasePage import BasePage
from selenium.webdriver.common.by import By


class FormPageLocators:
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
        self.fill_input(FormPageLocators.NAME_INPUT, name)

    def fill_inp_email(self, email):
        self.fill_input(FormPageLocators.EMAIL_INPUT, email)

    def fill_inp_pass(self, passw):
        self.fill_input(FormPageLocators.PASSWORD_INPUT, passw)

    def fill_inp_company(self, company):
        self.fill_input(FormPageLocators.COMPANY_INPUT, company)

    def fill_inp_website(self, website):
        self.fill_input(FormPageLocators.WEBSITE_INPUT, website)

    def fill_inp_country(self, country):
        self.select_value(FormPageLocators.COUNTRY_INPUT, country)

    def fill_inp_city(self, city):
        self.fill_input(FormPageLocators.CITY_INPUT, city)

    def fill_inp_addr1(self, addr1):
        self.fill_input(FormPageLocators.ADDRESS1_INPUT, addr1)

    def fill_inp_addr2(self, addr2):
        self.fill_input(FormPageLocators.ADDRESS2_INPUT, addr2)

    def fill_inp_state(self, state):
        self.fill_input(FormPageLocators.STATE_INPUT, state)

    def fill_inp_zip(self, zipcode):
        self.fill_input(FormPageLocators.ZIPCODE_INPUT, zipcode)

    def submit_form(self):
        self.click_element(FormPageLocators.SUBMIT_BUTTON)

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
        return "display" in self.get_element_attribute(FormPageLocators.SUBMIT_RES, "style")
