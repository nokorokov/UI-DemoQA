import time

from conftest import driver
from pages.alerts_frame_windows_page import (BrowserWindowsPage)


class TestAlertsFrameWindow:
    class TestBrowserWindows:

        def test_new_tab_or_new_window(self, driver):
            browser_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            result = browser_window_page.check_opened_new_tab_or_window()
            assert result == 'This is a sample page', \
                'the new tab or window has not opened or an incorrect tab or window is opened'
