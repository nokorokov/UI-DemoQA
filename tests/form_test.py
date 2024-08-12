import random
from conftest import driver
from pages.form_page import (FormPage)


class TestForm:
    class TestForm:
        def test_form(self, driver):
            text_box_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
            text_box_page.open()