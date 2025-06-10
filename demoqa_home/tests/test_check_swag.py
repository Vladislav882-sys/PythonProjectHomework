def test_check_icon(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    assert swag_page.exist_icon()

def test_check_username_field(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    assert swag_page.exist_username_field()

def test_check_password_field(browser):
    swag_page = SwagLabs(browser)
    swag_page.visit()
    assert swag_page.exist_password_field()