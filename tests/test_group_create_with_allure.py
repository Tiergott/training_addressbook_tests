import pytest


def test_group_create(app, login_admin, group, db):
    with pytest.allure.step("GIVEN a group list in Addressbook"):
        old_group_list = db.get_groups()
    with pytest.allure.step("WHEN I add {}".format(group)):
        app.open_group_page()
        app.create_group(group)
    with pytest.allure.step("THEN correct message is appeared"):
        assert app.group_message_page.is_this_page()
        assert "A new group has been entered into the address book." in app.group_message_page.message.text
        app.return_to_group_page()
    with pytest.allure.step("AND a new group list is equal to old group list with this new group"):
        new_group_list = db.get_groups()
        assert len(new_group_list) == len(old_group_list)+1, "There are not new group {}".format(group)
        assert group == new_group_list[-1],  "Group in db is not like one was created"
