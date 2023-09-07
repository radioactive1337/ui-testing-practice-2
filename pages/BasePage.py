import selenium.common
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


class BasePage:

    def __init__(self, driver, path):
        self.driver = driver
        self.url = f"https://www.lambdatest.com/selenium-playground/{path}"

    #  GET

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get_element(self, locator, time=5):
        """
        - wait some time and return webelement
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def get_elements(self, locator, time=5):
        """
        - wait some time and return webelements
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def get_element_attribute(self, locator, attr):
        return self.get_element(locator).get_attribute(attr)

    def get_elements_count(self, locator):
        """
        returns the number of elements found
        """
        value = len(self.driver.get_elements(locator))
        return value

    # OTHER
    def open(self):
        self.driver.get(self.url)

    def wait(self, time: float):
        sleep(time)

    def click_element(self, locator):
        self.get_element(locator).click()

    def clear_cookies(self):
        self.driver.delete_all_cookies()

    def fill_input(self, locator, value):
        """
        insert all text at once
        """
        self.get_element(locator).clear()
        self.get_element(locator).send_keys(value)

    def select_value(self, locator, value):
        return Select(self.get_element(locator)).select_by_value(value)

    def refresh_page(self):
        self.driver.refresh()
        try:
            self.driver.switch_to.alert.accept()
        except Exception:
            pass
        self.driver.switch_to.default_content()

    def verify_element_present(self, locator, time=5):
        """
        checking the presence of the element
        """
        try:
            self.get_element(locator, time)
            return True
        except selenium.common.TimeoutException:
            return False

    def scroll_page_to_top(self):
        self.driver.execute_script("window.scrollTo(0,0);")

    def scroll_page_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    def switch_to_main_window(self):
        windows_list = self.driver.window_handles
        self.driver.switch_to.window(windows_list[0])

    def switch_to_new_window(self):
        windows_list = self.driver.window_handles
        if len(windows_list) == 1:
            raise Exception('New window not found')
        self.driver.switch_to.window(windows_list[-1])
