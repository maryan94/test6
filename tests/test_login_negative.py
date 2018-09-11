from selene import config
from pages.login_page import LoginPage

config.browser_name = "chrome"


def test_login_negative_password():
    login_page = LoginPage()
    login_page.open()

    login_page.login_field.set(login_page.login)
    login_page.password_field.set(login_page.password)
    login_page.login_button.click()
    assert login_page.error.is_displayed()
