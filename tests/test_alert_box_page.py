from pages.AlertBoxPage import AlertBoxPage


def test_alertboxpage(driver):
    page = AlertBoxPage(driver, "javascript-alert-box-demo")
    page.open()
    page.show_alert_box()
    assert page.get_alert_hint() == "I am an alert box!", "the alert box text doesn't match"
    page.accept_alert()
    page.show_confirm_box()
    assert page.get_alert_hint() == "Press a button!", "the confirm box text doesn't match"
    page.dismiss_alert()
    page.show_prompt_box()
    assert page.get_alert_hint() == "Please enter your name", "the prompt box text doesn't match"
    page.enter_text_alert("qwe")
    page.accept_alert()
    page.wait(5)
