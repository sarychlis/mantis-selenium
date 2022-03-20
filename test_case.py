import os
import unittest

import dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase(unittest.TestCase):

    def setUp(self):
        dotenv.load_dotenv()
        self.driver = webdriver.Chrome('./chromedriver')

    def login(self):
        self.driver.maximize_window()
        self.driver.get(os.getenv('SITE_URL'))

        login_field = self.driver.find_element(By.ID, 'username')
        login_field.click()
        login_field.send_keys(os.getenv('USER_NAME'))

        self.driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/input[2]').click()

        password_field = self.driver.find_element(By.ID, 'password')
        password_field.send_keys(os.getenv('PASSWORD'))

        self.driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/input[3]').click()

    def goToProjectListPage(self):
        self.driver.find_element(By.XPATH, '//a[contains(@href,"manage_overview_page.php")]').click()
        self.driver.find_element(By.XPATH, '//*[@id="main-container"]/div[2]/div[3]/div/ul/li[3]/a').click()

    def tearDown(self):
        self.driver.close()
