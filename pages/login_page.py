from selene.api import *


class LoginPage(object):
    def __init__(self):
        self.login_field = s("input[type='email']")
        self.password_field = s("input[type='password']")
        self.login_button = s("button[type='submit']")
        self.error = s(by.text("Username or password is incorrect"))

        self.web_page = "https://dev-club.pixellot.tv/"
        self.login = "Superadmin@gmail.com"
        self.password = "superpixell"

    def open(self):
        browser.open_url(self.web_page)
