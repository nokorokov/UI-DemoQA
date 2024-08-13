import random

from pages.base_page import BasePage
from locators.alerts_frame_windows_locators import BrowserWindowsPageLocators


class BrowserWindowsPage(BasePage):
    locators = BrowserWindowsPageLocators()

    def check_opened_new_tab_or_window(self):
        buttons = [self.locators.NEW_WINDOW_BUTTON, self.locators.NEW_TAB_BUTTON]
        selected_buttons = random.choice(buttons)
        self.element_is_visible(selected_buttons).click()
        self.switch_window()
        text_title = self.element_is_present(self.locators.TITLE_NEW_TAB).text
        return text_title

