from selenium.webdriver import Keys

from .BasePage import BasePage
from selenium.webdriver.common.by import By


class SliderPageLocators:
    SLIDER1 = (By.XPATH, "(//input[@type='range'])[1]")
    SLIDER2 = (By.XPATH, "(//input[@type='range'])[2]")
    SLIDER3 = (By.XPATH, "(//input[@type='range'])[3]")
    SLIDER4 = (By.XPATH, "(//input[@type='range'])[4]")
    SLIDER5 = (By.XPATH, "(//input[@type='range'])[5]")
    SLIDER6 = (By.XPATH, "(//input[@type='range'])[6]")
    SLIDER7 = (By.XPATH, "(//input[@type='range'])[7]")
    SLIDER8 = (By.XPATH, "(//input[@type='range'])[8]")
    OUTPUT1 = (By.XPATH, "(//output)[1]")
    OUTPUT2 = (By.XPATH, "(//output)[2]")
    OUTPUT3 = (By.XPATH, "(//output)[3]")
    OUTPUT4 = (By.XPATH, "(//output)[4]")
    OUTPUT5 = (By.XPATH, "(//output)[5]")
    OUTPUT6 = (By.XPATH, "(//output)[6]")
    OUTPUT7 = (By.XPATH, "(//output)[7]")
    OUTPUT8 = (By.XPATH, "(//output)[8]")


class SliderPage(BasePage):
    def use_slider(self, slider, value):
        for j in range(value):
            self.get_element(slider).send_keys(Keys.RIGHT)

    def get_output_value(self, output):
        return self.get_element(output).text
