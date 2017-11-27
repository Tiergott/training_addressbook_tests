from models.group import Group
from pages.login_page import LoginPage
from pages.internal_page import InternalPage
from pages.groups_view_page import GroupViewPage
from pages.group_create_page import GroupCreatePage
from pages.group_message_page import GroupMessagePage


class AddressBookApp:
    def __init__(self, driver, base_url):
        self.wd = driver
        self.wd.implicitly_wait(5)
        self.wd.get(base_url)
        self.wd.maximize_window()
        self.login_page = LoginPage(driver, base_url)
        self.internal_page = InternalPage(driver, base_url)
        self.group_view_page = GroupViewPage(driver, base_url)
        self.group_create_page = GroupCreatePage(driver, base_url)
        self.group_message_page = GroupMessagePage(driver, base_url)

    def login(self, username, password):
        self.login_page.username_field.clear()
        self.login_page.username_field.send_keys(username)
        self.login_page.password_field.clear()
        self.login_page.password_field.send_keys(password)
        self.login_page.submit_button.click()

    def logout(self):
        self.internal_page.logout_button.click()

    def open_group_page(self):
        # Open group page
        self.internal_page.group_menu.click()

    def create_group(self, group):
        # Initialize group creation
        self.group_view_page.new_button_upper.click()
        # Fill group form
        self.group_create_page.group_name_field.clear()
        self.group_create_page.group_name_field.send_keys(group.name)
        self.group_create_page.group_header_field.clear()
        self.group_create_page.group_header_field.send_keys(group.header)
        self.group_create_page.group_footer_field.clear()
        self.group_create_page.group_footer_field.send_keys(group.footer)
        # Submit group creation
        self.group_create_page.submit_button.click()

    def return_to_group_page(self):
        # Return to group page
        self.group_message_page.return_to_group_page_link.click()

    def select_group_by_number(self, number):
        """" Return selected group """
        group_checkbox = self.group_view_page.groups_checkboxes[number]
        group_name = group_checkbox.get_attribute("title")[8:-1]
        group_id = int(group_checkbox.get_attribute("value"))
        group = Group(name=group_name, id=group_id)
        if not group_checkbox.is_selected():
            group_checkbox.click()
        return group

    def delete_group_by_number(self, number):
        self.select_group_by_number(number)
        self.group_view_page.delete_button_upper.click()

    def delete_group(self):
        self.group_view_page.delete_button_upper.click()

    def count_groups(self):
        self.open_group_page()
        return len(self.group_view_page.groups_checkboxes)

    def quit(self):
        self.wd.quit()
