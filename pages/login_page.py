from pages.page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):

    @property
    def username_field(self):
        return self.driver.find_element_by_name("user")

    @property
    def password_field(self):
        return self.driver.find_element_by_name("pass")

    @property
    def submit_button(self):
        return self.driver.find_element_by_xpath("//form[@id='LoginForm']/input[3]")

    def is_this_page(self):
        return self.is_element_present(By.NAME, "LoginForm")




if __name__=="__main__":
    from selenium import webdriver
    dr = webdriver.Chrome()
    dr.get("http://localhost/addressbook/")
    lg = LoginPage(driver=dr, base_url="http://localhost/addressbook/")
    lg.username_field.send_keys("admin")
    lg.username_field.send_keys("admin")
