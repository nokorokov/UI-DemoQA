from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators.widgets_locators import (AccordianPageLocators)


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    def check_accordian(self, accordian_num):
        accordian = {'first':
                         {'title': self.locators.FIRST_SECTION,
                          'content': self.locators.TEXT_FIRST_SECTION},
                     'second':
                         {'title': self.locators.SECOND_SECTION,
                          'content': self.locators.TEXT_SECOND_SECTION},
                     'third':
                         {'title': self.locators.THIRD_SECTION,
                          'content': self.locators.TEXT_THIRD_SECTION}
                     }
        self.go_to_element(self.element_is_present(accordian[accordian_num]['title']))
        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        section_title.click()
        try:
            self.go_to_element(self.element_is_present(accordian[accordian_num]['content']))
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            self.go_to_element(self.element_is_present(accordian[accordian_num]['content']))
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        return [section_title.text, len(section_content)]
