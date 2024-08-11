from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    # created from
    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = (By.CSS_SELECTOR, 'button[title="Expand all"]')
    ITEM_LIST = (By.CSS_SELECTOR, 'span[class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class = "rct-icon rct-icon-check"]')
    TITLE_ITEM = './/ancestor::span[@class = "rct-text"]'
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'span[class = "text-success"]')


class RadioButtonPageLocators:
    YES_RADIO_BUTTON = (By.CSS_SELECTOR, 'label[for="yesRadio"]')
    NO_RADIO_BUTTON = (By.CSS_SELECTOR, 'label[for="noRadio"]')
    IMPRESSIVE_RADIO_BUTTON = (By.CSS_SELECTOR, 'label[for="impressiveRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')


class WebTablePageLocators:
    # add person
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[id="addNewRecordButton"]')
    FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')

    # table
    FULL_PEOPLE_LIST = (By.CSS_SELECTOR, 'div[class="rt-tr-group"]')
    SEARCH_INPUT = (By.CSS_SELECTOR, 'input[id="searchBox"]')
    DELETE_BUTTON = (By.CSS_SELECTOR, 'span[title="Delete"]')
    ROW_PARENT = './/ancestor::div[@class="rt-tr-group"]'
    NO_ROWS_FOUND = (By.CSS_SELECTOR, 'div[class="rt-noData"]')
    COUNT_ROW_LIST = (By.CSS_SELECTOR, 'select[aria-label="rows per page"]')

    # update
    UPDATE_BUTTON = (By.CSS_SELECTOR, 'span[title="Edit"]')
    UPDATE_FIRSTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="firstName"]')
    UPDATE_LASTNAME_INPUT = (By.CSS_SELECTOR, 'input[id="lastName"]')
    UPDATE_EMAIL_INPUT = (By.CSS_SELECTOR, 'input[id="userEmail"]')
    UPDATE_AGE_INPUT = (By.CSS_SELECTOR, 'input[id="age"]')
    UPDATE_SALARY_INPUT = (By.CSS_SELECTOR, 'input[id="salary"]')
    UPDATE_DEPARTMENT_INPUT = (By.CSS_SELECTOR, 'input[id="department"]')
    UPDATE_SUBMIT_BUTTON = (By.CSS_SELECTOR, 'button[id="submit"]')


class ButtonPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="doubleClickBtn"]')
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, 'button[id="rightClickBtn"]')
    CLICK_ME_BUTTON = (By.XPATH, '//button[text()="Click Me"]')
    RESULT_DOUBLE_CLICK = (By.CSS_SELECTOR, 'p[id="doubleClickMessage"]')
    RESULT_RIGHT_CLICK = (By.CSS_SELECTOR, 'p[id="rightClickMessage"]')
    RESULT_CLICK_ME = (By.CSS_SELECTOR, 'p[id="dynamicClickMessage"]')


class LinksPageLocators:
    SIMPLE_LINK = (By.CSS_SELECTOR, 'a[id="simpleLink"]')
    BAD_REQUEST = (By.CSS_SELECTOR, 'a[id="bad-request"]')
    UNAUTHORIZED_REQUEST = (By.CSS_SELECTOR, 'a[id="unauthorized"]')
    FORBIDDEN_REQUEST = (By.CSS_SELECTOR, 'a[id=" forbidden"]')
    INVALID_URL_REQUEST = (By.CSS_SELECTOR, 'a[id=" invalid-url"]')


class UploadAndDownloadPageLocators:
    UPLOAD_INPUT = (By.CSS_SELECTOR, 'input[id="uploadFile"]')
    UPLOADED_FILE_PATH = (By.CSS_SELECTOR, 'p[id="uploadedFilePath"]')

    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, 'a[id="downloadButton"]')
