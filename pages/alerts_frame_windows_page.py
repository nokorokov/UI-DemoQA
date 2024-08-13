import random
import time

from selenium.common import UnexpectedAlertPresentException

from pages.base_page import BasePage
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators, AlertsPageLocators


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab_or_window(self):
        buttons = [self.locators.NEW_WINDOW_BUTTON, self.locators.NEW_TAB_BUTTON]
        selected_buttons = random.choice(buttons)
        self.element_is_visible(selected_buttons).click()
        self.switch_window()
        text_title = self.element_is_present(self.locators.TITLE_NEW_TAB).text
        return text_title


class AlertsPage(BasePage):
    locators = AlertsPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.switch_alert()
        return alert_window.text

    def check_alert_appear_after_5_sec(self):
        self.element_is_visible(self.locators.APPEAR_AFTER_5_SEC_BUTTON).click()
        time.sleep(5)
        try:
            alert_window = self.switch_alert()
            return alert_window.text
        except UnexpectedAlertPresentException:
            alert_window = self.switch_alert()
            return alert_window.text

    def check_confirm_box_appear(self):
        self.go_to_element(self.element_is_present(self.locators.CONFIRM_BOX_ALERT_BUTTON))
        self.element_is_visible(self.locators.CONFIRM_BOX_ALERT_BUTTON).click()
        alert_window = self.switch_alert()
        actions = {
            "accept": alert_window.accept,
            "dismiss": alert_window.dismiss
        }
        random_action = random.choice(list(actions.values()))
        random_action()
        text_result = self.element_is_clickable(self.locators.RESULT_CONFIRM_BOX).text
        return text_result

    def check_prompt_box_appear(self):
        text = f'nik{random.randint(0,999)}'
        self.go_to_element(self.element_is_present(self.locators.PROMPT_BOX_ALERT_BUTTON))
        self.element_is_visible(self.locators.PROMPT_BOX_ALERT_BUTTON).click()
        alert_window = self.switch_alert()
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_clickable(self.locators.RESULT_PROMPT_BOX).text
        return text, text_result




