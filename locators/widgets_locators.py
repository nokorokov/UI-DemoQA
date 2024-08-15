from selenium.webdriver.common.by import By


class AccordianPageLocators:
    FIRST_SECTION = (By.CSS_SELECTOR, 'div[id="section1Heading"]')
    TEXT_FIRST_SECTION = (By.CSS_SELECTOR, 'div[id="section1Content"] p')

    SECOND_SECTION = (By.CSS_SELECTOR, 'div[id="section2Heading"]')
    TEXT_SECOND_SECTION = (By.CSS_SELECTOR, 'div[id="section2Content"] p')

    THIRD_SECTION = (By.CSS_SELECTOR, 'div[id="section3Heading"]')
    TEXT_THIRD_SECTION = (By.CSS_SELECTOR, 'div[id="section3Content"] p')
