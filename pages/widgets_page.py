import random
import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from pages.base_page import BasePage
from locators.widgets_page_locators import (AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators,
                                            SliderPageLocators, ProgressBarPageLocators, TabsPageLocators,
                                            ToolTipsPageLocators, MenuPageLocators)


class AccordianPage(BasePage):
    locators = AccordianPageLocators()

    @allure.step('Check accordian')
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


class AutoCompletePage(BasePage):
    locators = AutoCompletePageLocators()

    @allure.step('Fill input multi')
    def fill_input_multi(self):
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2, 5))
        for color in colors:
            input_multi = self.element_is_clickable(self.locators.MULTI_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    @allure.step('Remove value from multi')
    def remove_value_from_multi(self):
        count_value_before = len(self.elements_are_present(self.locators.MULTI_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_VALUE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_present(self.locators.MULTI_VALUE))
        return count_value_before, count_value_after

    @allure.step('Check color in multi')
    def check_color_in_multi(self):
        color_list = self.elements_are_present(self.locators.MULTI_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    @allure.step('Fill single autocomplete')
    def fill_single_autocomplete(self):
        color = random.sample(next(generated_color()).color_name, k=1)
        single_input = self.element_is_clickable(self.locators.SINGLE_INPUT)
        single_input.send_keys(color)
        single_input.send_keys(Keys.ENTER)
        return color[0]

    @allure.step('Check color in single')
    def check_color_in_single(self):
        color = self.element_is_visible(self.locators.SINGLE_VALUE)
        return color.text


class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()

    @allure.step('Select date')
    def select_date(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after

    @allure.step('Select date and time')
    def select_date_and_time(self):
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATE_TIME_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_TIME_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_TIME_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_TIME_YEAR_LIST, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_TIME_TIME_LIST, date.time)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after


class SliderPage(BasePage):
    locators = SliderPageLocators()

    @allure.step('Change slider value')
    def change_slider_value(self):
        value_before = self.element_is_visible(self.locators.SLIDER_VALUE).get_attribute('value')
        slider_input = self.element_is_visible(self.locators.SLIDER_INPUT)
        self.action_drag_and_drop_by_offset(slider_input, random.randint(0, 100), 0)
        value_after = self.element_is_visible(self.locators.SLIDER_VALUE)
        return value_before, value_after.get_attribute('value')


class ProgressBarPage(BasePage):
    locators = ProgressBarPageLocators()

    @allure.step('Check progress')
    def check_progress(self):
        value_before = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        progress_bar_button = self.element_is_visible(self.locators.PROGRESS_BUTTON)
        progress_bar_button.click()
        time.sleep(random.randint(2, 10))
        progress_bar_button.click()
        value_after = self.element_is_present(self.locators.PROGRESS_BAR_VALUE).text
        return value_before, value_after


class TabsPage(BasePage):
    locators = TabsPageLocators()

    @allure.step('Check tabs')
    def check_tabs(self, name_tab):
        tabs = {'what':
                    {'title': self.locators.TABS_WHAT,
                     'content': self.locators.TABS_WHAT_CONTENT},
                'origin':
                    {'title': self.locators.TABS_ORIGIN,
                     'content': self.locators.TABS_ORIGIN_CONTENT},
                'use':
                    {'title': self.locators.TABS_USE,
                     'content': self.locators.TABS_USE_CONTENT},
                'more':
                    {'title': self.locators.TABS_MORE,
                     'content': self.locators.TABS_MORE_CONTENT}
                }
        button = self.element_is_visible(tabs[name_tab]['title'])
        button.click()
        what_content = self.element_is_visible(tabs[name_tab]['content']).text
        return button.text, len(what_content)


class ToolTipsPage(BasePage):
    locators = ToolTipsPageLocators()

    @allure.step('Get text form tool tips')
    def get_text_form_tool_tips(self, hover_element, wait_element):
        element = self.element_is_present(hover_element)
        self.action_move_to_element(element)
        self.element_is_visible(wait_element)
        time.sleep(1)
        tool_tip_text = self.element_is_visible(self.locators.TOOL_TIPS_INNERS)
        text = tool_tip_text.text
        return text

    @allure.step('Check tool tips')
    def check_tool_tips(self):
        tool_tip_text_button = self.get_text_form_tool_tips(self.locators.HOVER_BUTTON, self.locators.BUTTON_TT)
        tool_tip_text_field = self.get_text_form_tool_tips(self.locators.TEXT_FIELD, self.locators.TEXT_FIELD_TT)
        self.go_to_element(self.element_is_present(self.locators.CONTRARY_LINK))
        tool_tip_text_contrary = self.get_text_form_tool_tips(self.locators.CONTRARY_LINK, self.locators.CONTRARY_TT)
        self.go_to_element(self.element_is_present(self.locators.SECTION_LINK))
        tool_tip_text_section = self.get_text_form_tool_tips(self.locators.SECTION_LINK, self.locators.SECTION_TT)
        return tool_tip_text_button, tool_tip_text_field, tool_tip_text_contrary, tool_tip_text_section


class MenuPage(BasePage):
    locators = MenuPageLocators()

    @allure.step('Check menu')
    def check_menu(self):
        menu_item_list = self.elements_are_present(self.locators.MENU_ITEM_LIST)
        data = []
        for item in menu_item_list:
            self.action_move_to_element(item)
            data.append(item.text)
        return data
