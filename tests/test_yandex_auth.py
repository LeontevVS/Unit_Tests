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
        switcher_email = self.driver.find_element(By.XPATH, "//button[@data-type = 'login']")
        switcher_email.click()
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

    def find_test_element(self, element_id):
        element = None
        try:
            element = WebDriverWait(self.driver, 4).until(
            EC.presence_of_element_located((By.ID, element_id))
            )
        except Exception as ex:
            assert not isinstance(ex, TimeoutException)
        finally:
            assert not element is None

    def test_input_true_login(self):
        self.input_login(self.login)
        self.find_test_element('passp-field-passwd')

    def test_input_fake_login(self):
        self.input_login(self.fake_test_login)
        self.find_test_element('field:input-login:hint')

    def test_input_true_password(self):
        self.input_login(self.login)
        self.input_password(self.password)
        element = None
        try:
            element = WebDriverWait(self.driver, 4).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'UserID-Account'))
            )
        except Exception as ex:
            assert not isinstance(ex, TimeoutException)
        finally:
            assert not element is None

    # тест считается успешным если появляется надпись "неверный пароль". В случае появления капчи тест проваливается (не успел доработать)
    def test_input_fake_password(self):
        self.input_login(self.login)
        self.input_password(self.fake_test_password)
        self.find_test_element('field:input-passwd:hint')