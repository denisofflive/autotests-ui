from playwright.sync_api import sync_playwright, expect

# Открываем браузер с использованием Playwright
with sync_playwright() as playwright:
    # Запускаем Chromium браузер в обычном режиме (не headless)
    browser = playwright.chromium.launch(headless=False)
    # Создаем новый контекст браузера (новая сессия, которая изолирована от других)
    context = browser.new_context()
    # Открываем новую страницу в рамках контекста
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Указываем файл с сохраненным состоянием
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Сохраняем состояние браузера (куки и localStorage) в файл для дальнейшего использования
    context.storage_state(path="browser-state.json")

    # Проверяем, что отображается заголовок "Courses"
    courses = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses).to_be_visible()
    expect(courses).to_have_text("Courses")

    # Проверяем, что отображается Иконка
    icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    # Проверяем, что отображается блок "There is no results"
    block_results = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(block_results).to_be_visible()
    expect(block_results).to_have_text("There is no results")

    # Проверяем, что отображается текст "Results from the load test pipeline will be displayed here"
    text_results = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(text_results).to_be_visible()
    expect(text_results).to_have_text("Results from the load test pipeline will be displayed here")

    # Задержка для наглядности выполнения теста (не рекомендуется использовать в реальных автотестах)
    page.wait_for_timeout(5000)