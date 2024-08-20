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


class DatePickerPageLocators:
    DATE_INPUT = (By.CSS_SELECTOR, 'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR, 'select[class="react-datepicker__year-select"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR, 'select[class="react-datepicker__month-select"]')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR, 'div[class^="react-datepicker__day react-datepicker__day"]')

    DATE_TIME_INPUT = (By.CSS_SELECTOR, 'input[id="dateAndTimePickerInput"]')
    DATE_TIME_MONTH = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-read-view"]')
    DATE_TIME_YEAR = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-read-view"]')
    DATE_TIME_TIME_LIST = (By.CSS_SELECTOR, 'li[class^="react-datepicker__time-list-item"]')
    DATE_TIME_MONTH_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__month-option"]')
    DATE_TIME_YEAR_LIST = (By.CSS_SELECTOR, 'div[class="react-datepicker__year-option"]')


class SliderPageLocators:
    SLIDER_INPUT = (By.CSS_SELECTOR, 'input[class="range-slider range-slider--primary"]')
    SLIDER_VALUE = (By.CSS_SELECTOR, 'input[id="sliderValue"]')


class ProgressBarPageLocators:
    PROGRESS_BUTTON = (By.CSS_SELECTOR, 'button[id="startStopButton"]')
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR, 'div[class="progress-bar bg-info"]')
