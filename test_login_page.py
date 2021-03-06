from .pages.login_page import LoginPage


# def test_guest_should_see_login_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/accounts/login/"
#     page = LoginPage(browser, link)      # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                          # открываем страницу
#     page.should_be_login_form()          # выполняем метод страницы - переходим на страницу логина
#
# def test_guest_should_see_register_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/accounts/login/"
#     page = LoginPage(browser, link)        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()                            # открываем страницу
#     page.should_be_register_form()         # выполняем метод страницы - переходим на страницу логина

# def test_guest_should_open_login_url(browser):
#     link = link = "http://selenium1py.pythonanywhere.com/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     page.should_be_login_url()

def test_guest_should_see_login_page(browser):
    link = link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
