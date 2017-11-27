from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By


class GroupMessagePage(InternalPage):
    def is_this_page(self):
        return self.is_element_visible(By.CLASS_NAME, "msgbox")

    @property
    def message(self):
        return self.driver.find_element_by_class_name("msgbox")

    @property
    def return_to_group_page_link(self):
        return self.driver.find_element_by_link_text("group page")

