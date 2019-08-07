from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ContactsPage(BaseAction):
    add_name = By.XPATH, "//*[@text='姓名']"
    add_phone = By.XPATH, "//*[@text='电话']"

    def input_name(self, text):
        self.input(self.add_name, text)

    def input_phone(self, phone):
        self.input(self.add_phone, phone)