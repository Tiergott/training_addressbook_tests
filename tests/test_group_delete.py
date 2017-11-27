import random


def test_delete_group(app, login_admin, check_groups_exist, db):
    old_group_list = db.get_groups()
    index = random.randrange(app.count_groups())
    app.open_group_page()
    group = app.select_group_by_number(index)
    app.delete_group()
    assert app.group_message_page.is_this_page()
    assert "Group has been removed." in app.group_message_page.message.text
    app.return_to_group_page()
    new_group_list = db.get_groups()
    assert len(new_group_list) == len(old_group_list)-1
    assert group not in new_group_list

