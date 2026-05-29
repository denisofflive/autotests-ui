import pytest
from playwright.sync_api import expect, Page


# 1. Добавляем декоратор параметризации
@pytest.mark.parametrize(
    "email, password",
    [
        ("user.name@gmail.com", "password"),
        ("user.name@gmail.com", "  "),  # Два пробела в пароле
        ("  ", "password")  # Два пробела в email
    ],
    ids=[
        "Проверяем, что пользователь не может войти в систему с невалидными email и password",
        "Проверяем, что пользователь не может войти в систему с невалидным email, и пустым password",
        "Проверяем, что пользователь не может войти в систему с пустым email, и невалидным password"
    ]
)
# 2. Добавляем параметры в сигнатуру функции
@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
    """
    Проверка авторизации с неверными данными.
    Тест выполняется трижды с разными наборами email/password.
    """
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Используем переданные параметры для заполнения формы
    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill(email)

    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill(password)

    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')

    # Ожидаем, что алерт появится и содержит нужный текст
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
