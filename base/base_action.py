from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, location, timeout=10, poll=1):
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(location[0], location[1]))
        return element

    def click(self, location):
        self.find_element(location).click()

    def input(self, location, text):
        self.find_element(location).send_keys(text)

    def click_back(self):
        self.driver.press_keycode(4)

    def find_totast(self, message, timeout=5, poll=0.1):
        text = "//*[contains(@text, '" + message + "')]"
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element_by_xpath(text))
        return element.text

    def find_text(self, name, timeout=5, poll=0.1):
        text = '//*[@text="' + name + '"]'
        element = WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element_by_xpath(text))
        return element.text
