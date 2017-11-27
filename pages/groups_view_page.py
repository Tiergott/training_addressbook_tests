from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By


class GroupViewPage(InternalPage):
    def is_this_page(self):
        return self.is_element_visible(By.NAME, "new")

    @property
    def new_button_upper(self):
        return self.driver.find_element_by_name("new")

    @property
    def delete_button_upper(self):
        return self.driver.find_element_by_name("delete")

    @property
    def groups_checkboxes(self):
        return self.driver.find_elements_by_name("selected[]")
