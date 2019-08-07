from page.address_page import AddressPage
from page.contacts_page import ContactsPage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def address(self):
        return AddressPage(self.driver)

    @property
    def contacts(self):
        return ContactsPage(self.driver)