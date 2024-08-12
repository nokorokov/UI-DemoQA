from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators


class FormPage(BasePage):
    locators = FormPageLocators()
