from playwright.sync_api import Page, expect

from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Добавляем компонент Navbar
        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)

        self.students_chart_view = ChartViewComponent(page, identifier='students', chart_type='bar')
        self.activities_chart_view = ChartViewComponent(page, identifier='activities', chart_type='line')
        self.courses_chart_view = ChartViewComponent(page, identifier='courses', chart_type='pie')
        self.scores_chart_view = ChartViewComponent(page, identifier='scores', chart_type='scatter')
        self.dashboard_toolbar = DashboardToolbarViewComponent(page)

    def check_dashboard_title_visible(self):
        self.dashboard_toolbar.check_visible()

    def check_visible_students_chart(self):
        self.students_chart_view.check_visible(title='Students')

    def check_visible_courses_chart(self):
        self.students_chart_view.check_visible(title='Courses')

    def check_visible_activities_chart(self):
        self.students_chart_view.check_visible(title='Activities')

    def check_visible_scores_chart(self):
        self.students_chart_view.check_visible(title='Scores')
