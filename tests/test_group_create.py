def test_group_create(app, login_admin, group, db):
    old_list = db.get_groups()
    app.open_group_page()
    app.create_group(group)
    # TODO: verification of message
    app.return_to_group_page()
    new_list = db.get_groups()
    assert len(new_list) == len(old_list) + 1
    assert group == new_list[-1]
