import time

from conftest import driver
from pages.alerts_frame_windows_page import (BrowserWindowsPage, AlertsPage)


class TestAlertsFrameWindow:
    class TestBrowserWindows:

        def test_new_tab_or_new_window(self, driver):
            browser_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            result = browser_window_page.check_opened_new_tab_or_window()
            assert result == 'This is a sample page', \
                'the new tab or window has not opened or an incorrect tab or window is opened'

    class TestAlerts:

        def test_alerts(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_see_alert()
            assert alert_text == 'You clicked a button', 'Alert did not show up'

        def test_alert_appear_after_5_sec(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_alert_appear_after_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', 'Alert did not show up'

        def test_confirm_box_appear(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_confirm_box_appear()
            assert alert_text == 'You selected Ok' or 'You selected Cancel', 'Alert did not show up'

        def test_prompt_box_appear(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text, alert_text = alerts_page.check_prompt_box_appear()
            assert alert_text == f'You entered {text}', 'Alert did not show up'
