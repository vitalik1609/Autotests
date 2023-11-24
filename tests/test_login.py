# selenium 4
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage

def test_valid_auth(driver):
    login_page = LoginPage(driver)
    login_page.enter_username('test@protei.ru')
    login_page.enter_password('test')
    login_page.click_login_button()
    main_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h3')))
    assert main_title.is_displayed()
    assert main_title.text == 'Добро пожаловать!'

@pytest.mark.parametrize('email, password, xpath, warn_message', [('', '', 'emailFormatError', 'Неверный формат E-Mail'),
                                                                  ('test@protei.ru', '', 'KEKEKEKEKEKKEKE', 'Неверный E-Mail или пароль'),
                                                                  ('test@protei.ru', 'fdffdsfsf', 'KEKEKEKEKEKKEKE', 'Неверный E-Mail или пароль'),
                                                                  ('fgfgfgfdg', 'gfgfddfgfdgf', 'emailFormatError', 'Неверный формат E-Mail'),
                                                                  ('35435453', 'test', 'emailFormatError', 'Неверный формат E-Mail'),
                                                                  ('апрправап', 'test', 'emailFormatError', 'Неверный формат E-Mail'),
                                                                  ('!@#$%^&*()_-+=~`', 'фыыввыф', 'KEKEKEKEKEKKEKE', 'Неверный E-Mail или пароль')])

def test_negative_auth(driver, email, password, xpath, warn_message):
    login_page = LoginPage(driver)
    login_page.enter_username('test@protei.ru')
    login_page.enter_password('test')
    login_page.click_login_button()
    warn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f'//*[@id="{xpath}"]/p')))
    assert warn.is_displayed()
    assert warn.text == warn_message
