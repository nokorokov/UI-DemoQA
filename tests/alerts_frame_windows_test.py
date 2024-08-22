import time
import allure
from conftest import driver
from pages.alerts_frame_windows_page import (BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage,
                                             ModalDialogsPage)


@allure.suite("Alerts Frame Window")
class TestAlertsFrameWindow:
    @allure.feature('BrowserWindows')
    class TestBrowserWindows:

        @allure.title('Check new tab or window')
        def test_new_tab_or_new_window(self, driver):
            browser_window_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_window_page.open()
            result = browser_window_page.check_opened_new_tab_or_window()
            assert result == 'This is a sample page', \
                'the new tab or window has not opened or an incorrect tab or window is opened'

    @allure.feature('Alerts')
    class TestAlerts:

        @allure.title('Check alerts')
        def test_alerts(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_see_alert()
            assert alert_text == 'You clicked a button', 'Alert did not show up'

        @allure.title('Check alert appears after 5 sec')
        def test_alert_appear_after_5_sec(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_alert_appear_after_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds', 'Alert did not show up'

        @allure.title('Check confirm box appear')
        def test_confirm_box_appear(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alert_text = alerts_page.check_confirm_box_appear()
            assert alert_text == 'You selected Ok' or 'You selected Cancel', 'Alert did not show up'

        @allure.title('Check prompt box appear')
        def test_prompt_box_appear(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            text, alert_text = alerts_page.check_prompt_box_appear()
            assert alert_text == f'You entered {text}', 'Alert did not show up'

    @allure.feature('Frames')
    class TestFrames:

        @allure.title('Check frames')
        def test_frames(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['500px', '350px', 'This is a sample page'], 'frame does not exist'
            assert result_frame2 == ['100px', '100px', 'This is a sample page'], 'frame does not exist'

    @allure.feature('NestedFrames')
    class TestNestedFrames:

        @allure.title('Check nested frames')
        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent frame', 'Nested frame does not exist'
            assert child_text == 'Child Iframe', 'Nested frame does not exist'

    @allure.feature('ModalDialogs')
    class TestModalDialogs:

        @allure.title('Check modal dialogs')
        def test_modal_dialogs(self, driver):
            modal_dialogs_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_modal_dialogs()
            assert small[1] < large[1], 'Text from large dialog is less than text from small dialog'
            assert small[0] == 'Small Modal', 'The header is not "Small Modal"'
            assert large[0] == 'Large Modal', 'The header is not "Large Modal"'

        @allure.title('Check small modal dialog')
        def test_small_modal_dialog(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog_page.open()

        @allure.title('Check large modal dialog')
        def test_large_modal_dialog(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog_page.open()
