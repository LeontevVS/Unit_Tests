import dotenv
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import os
import time

class TestYandexAuth:
    dotenv.load_dotenv()
    login = os.getenv('YANDEX_LOGIN_OR_EMAIL')
    fake_test_login = 'efbsc'
    password = os.getenv('YANDEX_PASSWORD')
    fake_test_password = 'wvdscv'

    def setup_method(self):
        self.driver = webdriver.Edge()
        self.driver.get('https://passport.yandex.ru/auth/')

    def teardown_method(self):
        self.driver.close()
        self.driver.quit()

    def input_login(self, login):
        element_login = self.driver.find_element(By.NAME, 'login')
        element_login.send_keys(login)
        sign_in = self.driver.find_element(By.ID, 'passp:sign-in')
        sign_in.click()
        time.sleep(1.5)

    def input_password(self, password):
        element_password = self.driver.find_element(By.ID, 'passp-field-passwd')
        element_password.send_keys(password)
        sign_in = self.driver.find_element(By.ID, 'passp:sign-in')
        sign_in.click()
        time.sleep(1.5)

    def find_test_element(self, el_id):
        try:
            element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "passp-field-passwd"))
            )
        except Exception as ex:
            assert not isinstance(ex, TimeoutException)
        finally:
            assert not element is None

    def test_input_true_login(self):
        self.input_login(self.login)
        try:
            element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "passp-field-passwd"))
            )
        except Exception as ex:
            assert not isinstance(ex, TimeoutException)
        finally:
            assert not element is None

    def test_input_fake_login(self):
        self.input_login(self.fake_test_login)
        try:
            element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "field:input-login:hint"))
            )
        except Exception as ex:
            assert not isinstance(ex, TimeoutException)
        finally:
            assert not element is None

    def test_input_true_password(self):
        self.input_login(self.fake_test_login)
        try:
            element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "UserID-Account"))
            )
        except Exception as ex:
            assert not isinstance(ex, TimeoutException)
        finally:
            assert not element is None

    def test_input_fake_password(self):
        self.input_login(self.login)
        self.input_password(self.fake_test_password)
        try:
            element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ID, "field:input-passwd:hint"))
            )
        except Exception as ex:
            assert not isinstance(ex, TimeoutException)
        finally:
            assert not element is None

class YandexAuth:
    def __init__(self):

        login = self.driver.find_element(By.NAME, 'login')
        # login.send_keys('vitalijleont@yandex.ru')
        login.send_keys('efbsc')
        sign_in = self.driver.find_element(By.ID, 'passp:sign-in')
        sign_in.click()
        time.sleep(1.5)
        # password = self.driver.find_element(By.ID, 'passp-field-passwd')
        # password.send_keys('1234')
        text = self.driver.find_element(By.ID, 'field:input-login:hint').text
        print(text)  


# tya = TestYandexAuth()
# tya.setup_method()
# tya.test_input_fake_password()
# tya.teardown_method() 