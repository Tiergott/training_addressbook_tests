from pytest_bdd import given, when, then
from models.group import Group
import random


@given("a group list in Addressbook")
def old_group_list(db):
    return db.get_groups()


@given("a new group with <name>, <header>, <footer>")
def group(name, header, footer):
    return Group(name, header, footer)


@when("I add this group")
def create_group(app, login_admin, group):
    app.open_group_page()
    app.create_group(group)
    app.return_to_group_page()


@then("a new group list is equal to old group list with this new group")
def verify_group_created(db, old_group_list, group):
    new_group_list = db.get_groups()
    assert len(new_group_list) == len(old_group_list) + 1, "There are not new group {}".format(group)
    assert group == new_group_list[-1],  "Group in db is not like one was created"


@given("a non-empty group list in Addressbook")
def non_empty_old_group_list(db, check_groups_exist):
    return db.get_groups()


@given("a selected random group in this list")
def selected_random_group(app, login_admin):
    index = random.randrange(app.count_groups())
    return app.select_group_by_number(index)


@when("I delete this group")
def delete_group(app, selected_random_group):
    app.delete_group()
    app.return_to_group_page()


@then("a new list is equal to old list without this group")
def verify_group_deleted(db, non_empty_old_group_list, selected_random_group):
    new_group_list = db.get_groups()
    assert len(new_group_list) == len(non_empty_old_group_list)-1
    assert selected_random_group not in new_group_list
