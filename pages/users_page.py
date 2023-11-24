from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

'''Страница Пользователи'''
class UsersPage:

    def __init__(self, driver):
        self.driver = driver

    def log_in(self):
        self.driver.find_element(By.ID, 'loginEmail').send_keys('test@protei.ru')
        self.driver.find_element(By.ID, 'loginPassword').send_keys('test')
        self.driver.find_element(By.ID, 'authButton').click()

    def go_to_users_by_click(self):
        users_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'menuUsersOpener')))
        users_button.click()
        users_button.click()

    def go_to_users_by_dropdown(self):
        users_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, 'menuUsersOpener')))
        users_button.click()
        table_button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="menuUsers"]')))
        table_button.click()

    def check_table(self):
        table = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="usersPage"]')))
        return table

    def click_add_user_button(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, 'addUser'))).click()


    def find_main_title(self):
        main_title = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'uk-legend')))
        return main_title

    EMAIL_FIELD = (By.ID, 'dataEmail')
    PASSWORD_FIELD = (By.ID, 'dataPassword')
    USERNAME_FIELD = (By.ID, 'dataName')
    GENDER_BUTTON = (By.XPATH, '//*[@id="dataGender"]')
    MALE = (By.XPATH, '//*[@id="dataGender"]/option[1]')
    FEMALE = (By.XPATH, '//*[@id="dataGender"]/option[2]')
    ADD_BUTTON = (By.XPATH, '//*[@id="dataSend"]')

    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)

    def choose_gender(self, gender):
        self.driver.find_element(*self.GENDER_BUTTON).click()
        if gender == 'male':
            self.driver.find_element(*self.MALE).click()
        elif gender == 'female':
            self.driver.find_element(*self.FEMALE).click()

    def click_radiobutton(self, radiobtn_number):
        self.driver.find_element(By.ID, f'dataSelect1{radiobtn_number}').click()

    def click_checkbox(self, checkbox_number):
        self.driver.find_element(By.ID, f'dataSelect2{checkbox_number}').click()

    def click_add_button(self):
        button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="dataSend"]')))
        button.click()

    def find_notification(self):
        notif = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div[1]')))
        return notif

