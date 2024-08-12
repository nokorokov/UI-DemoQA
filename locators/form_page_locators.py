from selenium.webdriver.common.by import By


class FormPageLocators:
    # inputs
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    NUMBER_INPUT = (By.CSS_SELECTOR, 'input[id="userNumber"]')
    BIRTHDATE_INPUT = (By.CSS_SELECTOR, 'input[id="dateOfBirthInput"]')
    SUBJECT_INPUT = (By.CSS_SELECTOR, 'input[id="subjectsInput"]')

    # text-areas
    ADDRESS_TEXT_AREA = (By.CSS_SELECTOR, 'textarea[id="currentAddress"]')

    # radio
    MALE_RADIO = (By.CSS_SELECTOR, 'label[for ="gender-radio-1"]')
    FEMALE_RADIO = (By.CSS_SELECTOR, 'label[for ="gender-radio-2"]')
    OTHER_RADIO = (By.CSS_SELECTOR, 'label[for ="gender-radio-3"]')

    #checkboxes
    SPORT_CHECKBOX = (By.CSS_SELECTOR, 'label[for ="gender-radio-1"]')
    READING_CHECKBOX = (By.CSS_SELECTOR, 'label[for ="gender-radio-2"]')
    MUSIC_CHECKBOX = (By.CSS_SELECTOR, 'label[for ="gender-radio-3"]')

    #upload_file
    UPLOAD_INPUT = (By.CSS_SELECTOR, 'input[id="uploadPicture"]')

    #dropdown

    #button
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

    #succesfull form
    SUCCESS_FORM_TITLE = (By.CSS_SELECTOR, 'div[class="modal-title h4"]')