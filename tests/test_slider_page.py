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
    assert page.get_output_value(SliderPageLocators.OUTPUT1) == "45", "value of slider 1 isn't correct"
    assert page.get_output_value(SliderPageLocators.OUTPUT2) == "50", "value of slider 2 isn't correct"
    assert page.get_output_value(SliderPageLocators.OUTPUT3) == "35", "value of slider 3 isn't correct"
    assert page.get_output_value(SliderPageLocators.OUTPUT4) == "60", "value of slider 4 isn't correct"
