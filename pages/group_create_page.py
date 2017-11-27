from pages.internal_page import InternalPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_to_be_clickable


class GroupCreatePage(InternalPage):
    def is_this_page(self):
        return self.is_element_visible(By.CSS_SELECTOR, '#content > form > input[name="submit"]')

    @property
    def group_name_field(self):
        return self.driver.find_element_by_name("group_name")

    @property
    def group_header_field(self):
        return self.driver.find_element_by_name("group_header")

    @property
    def group_footer_field(self):
        return self.driver.find_element_by_name("group_footer")

    @property
    def submit_button(self):
        return self.wait.until(element_to_be_clickable((By.NAME, "submit")))

