def test_group_create(app, login_admin, group, db):
    old_group_list = db.get_groups()
    app.open_group_page()
    app.create_group(group)
    assert app.group_message_page.is_this_page()
    assert "A new group has been entered into the address book." in app.group_message_page.message.text
    app.return_to_group_page()
    new_group_list = db.get_groups()
    assert len(new_group_list) == len(old_group_list)+1, "There are not new group {}".format(group)
    assert group == new_group_list[-1],  "Group in db is not like one was created"
