def test_login(app):
    app.login(username="admin", password="secret")
    # app.login_page.username_field.clear()
    # app.login_page.username_field.send_keys("admin")
    # app.login_page.password_field.clear()
    # app.login_page.password_field.send_keys("secret")
    # app.login_page.submit_button.click()
    assert app.internal_page.is_this_page()
    assert app.internal_page.username_indicator == "admin"
    app.logout()
    assert app.login_page.is_this_page()