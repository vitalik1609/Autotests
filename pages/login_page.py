from selenium.webdriver.common.by import By

'''Страница Авторизации'''
class LoginPage:

    USERNAME_FIELD = (By.ID,'loginEmail')
    PASSWORD_FIELD = (By.ID, 'loginPassword')
    LOGIN_BUTTON = (By.ID, 'authButton')

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()