import pytest
from pages.users_page import UsersPage



'''Проверяем наличие таблицы на страницу Пользователи'''
def test_check_table(driver):
    users_page = UsersPage(driver)
    users_page.log_in()
    users_page.go_to_users_by_click()
    table = users_page.check_table()
    assert table.is_displayed()

    users_page.go_to_users_by_dropdown()
    table = users_page.check_table()
    assert table.is_displayed()


'''Добавляем новых пользователей'''
@pytest.mark.parametrize('email, password, username, gender, radiobuttons, checkboxes', [('test1@protei.ru', 'test123', 'Angelina', 'female', ('2', ), ('1', '2', '3')),
                                                                                         ('test2@protei.ru', '12345', 'Vitalik', 'male', ('1', '2'), ('2', '3'))])
def test_add_user(driver, email, password, username, gender, radiobuttons, checkboxes):
    users_page = UsersPage(driver)
    users_page.log_in()
    users_page.go_to_users_by_click()
    users_page.click_add_user_button()
    main_title = users_page.find_main_title()
    assert main_title.is_displayed()
    assert main_title.text == 'Добавление пользователя'
    users_page.enter_email(email)
    users_page.enter_password(password)
    users_page.enter_username(username)
    users_page.choose_gender(gender)
    #driver.execute_script("document.body.style.zoom='50%'")
    for radiobutton in radiobuttons:
        users_page.click_radiobutton(radiobutton)
    for checkbox in checkboxes:
        users_page.click_checkbox(checkbox)
    users_page.click_add_button()

    success_notif = users_page.find_notification()
    assert success_notif.is_displayed()
    assert success_notif.text == 'Данные добавлены.'




