import pytest
from pages.SliderPage import SliderPage
from pages.SliderPage import SliderPageLocators


@pytest.mark.parametrize("val1, val2, val3, val4", [(40, 30, 20, 10)])
def test_sliderpage(driver, val1, val2, val3, val4):
    page = SliderPage(driver, "drag-drop-range-sliders-demo")
    page.open()
    page.use_slider(SliderPageLocators.SLIDER1, val1)
    page.use_slider(SliderPageLocators.SLIDER2, val2)
    page.use_slider(SliderPageLocators.SLIDER3, val3)
    page.use_slider(SliderPageLocators.SLIDER4, val4)
    assert page.get_output_value(SliderPageLocators.OUTPUT1) == "45"
    assert page.get_output_value(SliderPageLocators.OUTPUT2) == "50"
    assert page.get_output_value(SliderPageLocators.OUTPUT3) == "35"
    assert page.get_output_value(SliderPageLocators.OUTPUT4) == "60"
