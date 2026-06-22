import allure
import pytest

from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.epics import AllureEpic # Импортируем enum AllureEpic
from tools.allure.features import AllureFeature # Импортируем enum AllureFeature
from tools.allure.stories import AllureStory # Импортируем enum AllureStory
from tools.allure.tags import AllureTag
from allure_commons.types import Severity
from tools.allure.parent_suite import AllureParentSuite
from tools.allure.sub_suite import AllureSubSuite
from tools.allure.suite import AllureSuite
from config import settings
from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS) # Добавили epic
@allure.feature(AllureFeature.AUTHENTICATION) # Добавили feature
@allure.story(AllureStory.REGISTRATION) # Добавили story
@allure.parent_suite(AllureParentSuite.LMS)
@allure.suite(AllureSuite.AUTHENTICATION)
@allure.sub_suite(AllureSubSuite.REGISTRATION)
class TestRegistration:

    @allure.title("Registration with correct email, username and password")
    @allure.severity(Severity.CRITICAL)
    def test_successful_registration(self, dashboard_page: DashboardPage, registration_page: RegistrationPage):
        registration_page.visit(AppRoute.REGISTRATION)
        registration_page.registration_form.fill(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.registration_form.check_visible(
            email=settings.test_user.email,
            username=settings.test_user.username,
            password=settings.test_user.password
        )
        registration_page.click_registration_button()

        dashboard_page.dashboard_toolbar_view.check_visible()
