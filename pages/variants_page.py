from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

'''Страница Варианты'''
class VariantsPage:

    def __init__(self, driver):
        self.driver = driver

    def log_in(self):
        self.driver.find_element(By.ID, 'loginEmail').send_keys('test@protei.ru')
        self.driver.find_element(By.ID, 'loginPassword').send_keys('test')
        self.driver.find_element(By.ID, 'authButton').click()
        var_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '// *[ @ id = "menuMore"]')))
        var_button.click()


    def find_logo(self):
        logo = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/img')))
        return logo

    def find_main_title(self):
        main_title = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'h3')))
        return main_title

    def find_second_title(self):
        second_title = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/p[1]')))
        return second_title

    def find_third_title(self):
        third_title = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/p[2]')))
        return third_title