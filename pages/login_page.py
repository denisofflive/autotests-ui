from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.authentication.login_form_component import LoginFormComponent


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_form = LoginFormComponent(page)

        self.login_alert = self.page.get_by_test_id('login-page-wrong-email-or-password-alert')
        self.login_button = self.page.get_by_test_id('login-page-login-button')


    def fill(self, email: str, password: str):
        self.login_form.fill(email=email, password=password)

    def check_visible(self):
        self.login_form.check_visible()

    def check_alert(self):
        expect(self.login_alert).to_be_visible()
        expect(self.login_alert).to_have_text('Wrong email or password')

    def click_login_button(self):
        expect(self.login_button).to_be_visible()
        self.login_button.click()
