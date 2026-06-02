import pytest

from pages.login_page import LoginPage

@pytest.mark.authorization
@pytest.mark.regression
@pytest.mark.parametrize('email, password', [('321','321'), ('4324234','324234234')])
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')
    login_page.check_visible()
    login_page.fill(email=email, password=password)
    login_page.click_login_button()
    login_page.check_alert()
