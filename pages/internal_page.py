from pages.page import Page
from selenium.webdriver.common.by import By


class InternalPage(Page):
    @property
    def logout_button(self):
        return self.driver.find_element_by_xpath("//div/div[1]/form/a")

    @property
    def username_indicator(self):
        return self.driver.find_element_by_xpath('//*[@id="top"]/form/b').text.strip("()")

    def is_this_page(self):
        return self.is_element_visible(By.NAME, "logout")
