import time

from base.base_data import data
from base.base_driver import get_driver
import pytest

from page.page import Page


class TestContacts:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(4)
        self.driver.quit()

    @pytest.mark.parametrize("args", data("contacts_data.yaml", "test_add_contacts"))
    def test_add_contacts(self, args):
        name = args["name"]
        phone = args["phone"]
        message = args["text"]
        self.page.address.click_add_btn()
        self.page.contacts.input_name(name)
        self.page.contacts.input_phone(phone)
        self.page.contacts.click_back()
        text = self.page.contacts.find_totast(message)
        assert message in text
        time.sleep(3)
        assert name == self.page.contacts.find_text(name)
