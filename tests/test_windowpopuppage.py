from pages.WindowPopUpPage import WindowPopupPage


def test_windowpopuppage(driver):
    page = WindowPopupPage(driver, "window-popup-modal-demo")
    page.open()
    page.open_twitter_window()
    page.switch_to_new_window()
    assert "twitter" in page.get_url()
    page.close_current_window()
    page.switch_to_main_window()
    page.open_facebook_window()
    page.switch_to_new_window()
    assert "facebook" in page.get_url()
    page.close_current_window()
    page.switch_to_main_window()
    page.open_linkedin_window()
    page.switch_to_new_window()
    assert "linkedin" in page.get_url()
