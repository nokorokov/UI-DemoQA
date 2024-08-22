import random
import time

import allure
from selenium.common import UnexpectedAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.alerts_frame_windows_locators import (BrowserWindowsPageLocators, AlertsPageLocators, FramesPageLocators,
                                                    NestedFramesPageLocators, ModalDialogsPageLocators)


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    @allure.step('Check opened new tab or window')
    def check_opened_new_tab_or_window(self):
        buttons = [self.locators.NEW_WINDOW_BUTTON, self.locators.NEW_TAB_BUTTON]
        selected_buttons = random.choice(buttons)
        with allure.step('click button and switch to window'):
            self.element_is_visible(selected_buttons).click()
            self.switch_to_window()
        text_title = self.element_is_present(self.locators.TITLE_NEW_TAB).text
        return text_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    @allure.step('Click and see alert')
    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        alert_text = alert_window.text
        alert_window.accept()
        return alert_text

    @allure.step('Check appear alert after 5 second and check alert text')
    def check_alert_appear_after_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_AFTER_5_SEC_BUTTON).click()
        alert_window = self.switch_to_alert()
        alert_text = alert_window.text
        alert_window.accept()
        return alert_text

    @allure.step('Check accept and dismiss alert')
    def check_confirm_box_appear(self):
        self.go_to_element(self.element_is_present(self.locators.CONFIRM_BOX_ALERT_BUTTON))
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        actions = {
            "accept": alert_window.accept,
            "dismiss": alert_window.dismiss
        }
        random_action = random.choice(list(actions.values()))
        random_action()
        text_result = self.element_is_clickable(self.locators.RESULT_CONFIRM_BOX).text
        return text_result

    @allure.step('Check prompt box appear')
    def check_prompt_box_appear(self):
        text = f'nik{random.randint(0, 999)}'
        self.go_to_element(self.element_is_present(self.locators.PROMPT_BOX_ALERT_BUTTON))
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.switch_to_alert()
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_clickable(self.locators.RESULT_PROMPT_BOX).text
        return text, text_result


class FramesPage(BasePage):
    locators = FramesPageLocators()

    @allure.step('Switch and check frame')
    def check_frame(self, frame_num):
        if frame_num == 'frame1':
            frame = self.element_is_present(self.locators.FIRST_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.switch_to_frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [width, height, text]

        if frame_num == 'frame2':
            frame = self.element_is_present(self.locators.SECOND_FRAME)
            width = frame.get_attribute('width')
            height = frame.get_attribute('height')
            self.switch_to_frame(frame)
            text = self.element_is_present(self.locators.TITLE_FRAME).text
            self.driver.switch_to.default_content()
            return [width, height, text]


class NestedFramesPage(BasePage):
    locators = NestedFramesPageLocators()

    @allure.step('Switch and check nested frame')
    def check_nested_frame(self):
        parent_frame = self.element_is_present(self.locators.PARENT_FRAME)
        self.switch_to_frame(parent_frame)
        parent_text = self.element_is_present(self.locators.TEXT_PARENT_FRAME).text
        child_frame = self.element_is_present(self.locators.CHILD_FRAME)
        self.switch_to_frame(child_frame)
        child_text = self.element_is_present(self.locators.TEXT_CHILD_FRAME).text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    locators = ModalDialogsPageLocators()

    @allure.step('Check modal dialogs')
    def check_modal_dialogs(self):
        self.element_is_visible(self.locators.SMALL_MODAL_BUTTON).click()
        title_small = self.element_is_visible(self.locators.TITLE_SMALL_MODAL).text
        body_small_text = self.element_is_visible(self.locators.TEXT_SMALL_DIALOG).text
        self.element_is_visible(self.locators.CLOSE_SMALL_MODAL_BUTTON).click()

        self.element_is_visible(self.locators.LARGE_MODAL_BUTTON).click()
        title_large = self.element_is_visible(self.locators.TITLE_LARGE_MODAL).text
        body_large_text = self.element_is_visible(self.locators.TEXT_LARGE_DIALOG).text

        return [title_small, len(body_small_text)], [title_large, len(body_large_text)]
