from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class AddressPage(BaseAction):
    add_btn = By.ID, "com.android.contacts:id/floating_action_button"

    def click_add_btn(self):
        self.click(self.add_btn)