import random
from selenium.webdriver.common.by import By


class FormPageLocators:
    # inputs
    FIRST_NAME = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LAST_NAME = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    GENDER = (By.CSS_SELECTOR, f'div[class*="custom-control"] label[for="gender-radio-{random.randint(1,3)}"]')
    MOBILE_NUMBER = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    BIRTHDATE = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    SUBJECT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')

    # checkboxes
    HOBBIES = (By.CSS_SELECTOR,
               f'div[class*="custom-control"] label[for="hobbies-checkbox-{random.randint(1, 3)}"]')

    # upload_file
    FILE_INPUT = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')

    # text-areas
    CURRENT_ADDRESS = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')

    # dropdown
    SELECT_STATE = (By.CSS_SELECTOR, 'div[id="state"]')
    STATE_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-3-input"]')
    SELECT_CITY = (By.CSS_SELECTOR, 'div[id="city"]')
    CITY_INPUT = (By.CSS_SELECTOR, 'input[id="react-select-4-input"]')

    # button
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

    # successful form
    SUCCESS_FORM_TITLE = (By.CSS_SELECTOR, 'div[class="modal-title h4"]')
    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')