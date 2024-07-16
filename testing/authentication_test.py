import os
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['DJANGO_SETTINGS_MODULE'] = 'harmonia.settings'

class AuthenticationTest(StaticLiveServerTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        driver = self.driver
        driver.get(f'{self.live_server_url}/authentication/signup/')

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )

        username_input = driver.find_element(By.NAME, 'username')
        password1_input = driver.find_element(By.NAME, 'password1')
        password2_input = driver.find_element(By.NAME, 'password2')

        username_input.send_keys('testuser')
        password1_input.send_keys('testpassword123')
        password2_input.send_keys('testpassword123')
        password2_input.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(
            EC.title_contains('Home')
        )

        self.assertIn('Home', driver.title)

    def test_user_login(self):
        driver = self.driver
        driver.get(f'{self.live_server_url}/authentication/login/')

        # Use explicit waits to ensure elements are available
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )

        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')

        username_input.send_keys('testuser')
        password_input.send_keys('testpassword123')
        password_input.send_keys(Keys.RETURN)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )

        self.assertIn('Feed', driver.page_source)



    def test_user_login(self):
        driver = self.driver
        driver.get('http://localhost:8000/authentication/login/')
        
        username_input = driver.find_element(By.NAME, 'username')
        password_input = driver.find_element(By.NAME, 'password')

        username_input.send_keys('testuser')
        password_input.send_keys('testpassword123')

        password_input.send_keys(Keys.RETURN)
        time.sleep(2)

        self.assertIn('Feed', driver.page_source)

if __name__ == "__main__":
    unittest.main()