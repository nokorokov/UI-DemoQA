from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_SECTION = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    TEXT_FIRST_SECTION = (By.CSS_SELECTOR, 'div[id="section1Content"] p')

    SECOND_SECTION = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    TEXT_SECOND_SECTION = (By.CSS_SELECTOR, 'div[id="section2Content"] p')

    THIRD_SECTION = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    TEXT_THIRD_SECTION = (By.CSS_SELECTOR, 'div[id="section3Content"] p')


class AutoCompletePageLocators:
    MULTI_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteMultipleInput"]')
    MULTI_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_VALUE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')


    SINGLE_INPUT = (By.CSS_SELECTOR, 'input[id="autoCompleteSingleInput"]')
    SINGLE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')



