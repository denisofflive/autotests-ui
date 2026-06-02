from playwright.sync_api import Page, expect

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.image_upload_widget = ImageUploadWidgetComponent(page, identifier='create-course-preview')
        self.create_course_form = CreateCourseFormComponent(page)
        self.create_course_toolbar = CreateCourseToolbarViewComponent(page)
        self.create_course_exercises_toolbar = CreateCourseExercisesToolbarViewComponent(page)
        self.empty_view = EmptyViewComponent(page, identifier='create-course-exercises')
        self.create_exercises_course_form = CreateCourseExerciseFormComponent(page)
        self.exercises_empty_view = EmptyViewComponent(page, identifier='create-course-exercises')

    def check_visible_create_course_title(self, is_create_course_disabled: bool = True):
        self.create_course_toolbar.check_visible(is_create_course_disabled)

    def click_create_course_button(self):
        self.create_course_toolbar.click_create_course_button()

    def check_visible_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_form.check_visible(
            title=title,
            estimated_time=estimated_time,
            description=description,
            max_score=max_score,
            min_score=min_score
        )

    def fill_create_course_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.create_course_form.fill(
            title=title,
            estimated_time=estimated_time,
            description=description,
            max_score=max_score,
            min_score=min_score,
        )

    def check_visible_exercises(self):
        self.create_course_exercises_toolbar.check_visible()

    def click_create_exercises_button(self):
        self.create_course_exercises_toolbar.click_create_exercise_button()

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )
