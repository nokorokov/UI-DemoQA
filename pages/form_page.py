import os
from selenium.webdriver import Keys

from generator.generator import generated_person, generated_file
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators


class FormPage(BasePage):
    locators = FormPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        filename, path = generated_file()
        self.go_to_element(self.element_is_present(self.locators.FIRST_NAME))
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(person.firstname)

        self.go_to_element(self.element_is_present(self.locators.LAST_NAME))
        self.element_is_visible(self.locators.LAST_NAME).send_keys(person.lastname)

        self.go_to_element(self.element_is_present(self.locators.EMAIL))
        self.element_is_visible(self.locators.EMAIL).send_keys(person.email)

        self.go_to_element(self.element_is_present(self.locators.GENDER))
        self.element_is_visible(self.locators.GENDER).click()

        self.go_to_element(self.element_is_present(self.locators.MOBILE_NUMBER))
        self.element_is_visible(self.locators.MOBILE_NUMBER).send_keys(person.mobile)

        self.go_to_element(self.element_is_present(self.locators.SUBJECT))
        self.element_is_visible(self.locators.SUBJECT).send_keys('Maths')
        self.element_is_visible(self.locators.SUBJECT).send_keys(Keys.RETURN)

        self.go_to_element(self.element_is_present(self.locators.HOBBIES))
        self.element_is_visible(self.locators.HOBBIES).click()

        self.element_is_present(self.locators.FILE_INPUT).send_keys(str(path))
        os.remove(str(path))

        self.go_to_element(self.element_is_present(self.locators.CURRENT_ADDRESS))
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(person.current_address)

        self.go_to_element(self.element_is_present(self.locators.SELECT_STATE))
        self.element_is_visible(self.locators.SELECT_STATE).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)

        self.element_is_visible(self.locators.SELECT_CITY).click()
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)

        self.go_to_element(self.element_is_present(self.locators.SUBMIT_BUTTON))
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return person

    def form_result(self):
        result_list = self.elements_are_present(self.locators.RESULT_TABLE)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data




