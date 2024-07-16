import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AuthenticationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        driver.get('http://localhost:8000/register/')
        
        username_input = driver.find_element(By.NAME, 'username')
        email_input = driver.find_element(By.NAME, 'email')
        password1_input = driver.find_element(By.NAME, 'password1')
        password2_input = driver.find_element(By.NAME, 'password2')

        username_input.send_keys('testuser')
        email_input.send_keys('testuser@example.com')
        password1_input.send_keys('testpassword123')
        password2_input.send_keys('testpassword123')

        password2_input.send_keys(Keys.RETURN)
        time.sleep(2)

        self.assertIn('Home', driver.title)