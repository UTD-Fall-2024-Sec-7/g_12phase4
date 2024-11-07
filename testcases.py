from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://example.com/login')  # Replace with your login URL
        self.driver.maximize_window()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_valid_login(self):
        driver = self.driver
        driver.find_element(By.ID, 'username').send_keys('validuser')
        driver.find_element(By.ID, 'password').send_keys('validpassword')
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(2)
        self.assertTrue(driver.find_element(By.ID, 'logout-button'))

    def test_min_length_credentials(self):
        driver = self.driver
        driver.find_element(By.ID, 'username').send_keys('ab')
        driver.find_element(By.ID, 'password').send_keys('12')
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(2)
        self.assertTrue(driver.find_element(By.ID, 'error-message'))

    def test_alphanumeric_credentials(self):
        driver = self.driver
        driver.find_element(By.ID, 'username').send_keys('user123')
        driver.find_element(By.ID, 'password').send_keys('pass456')
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(2)
        self.assertTrue(driver.find_element(By.ID, 'logout-button'))

    def test_incorrect_password(self):
        driver = self.driver
        driver.find_element(By.ID, 'username').send_keys('validuser')
        driver.find_element(By.ID, 'password').send_keys('wrongpassword')
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, 'error-message').text
        self.assertIn('Invalid username or password', error_message)

    def test_incorrect_username(self):
        driver = self.driver
        driver.find_element(By.ID, 'username').send_keys('wronguser')
        driver.find_element(By.ID, 'password').send_keys('validpassword')
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, 'error-message').text
        self.assertIn('Invalid username or password', error_message)

    def test_empty_username(self):
        driver = self.driver
        driver.find_element(By.ID, 'username').send_keys('')
        driver.find_element(By.ID, 'password').send_keys('validpassword')
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, 'error-message').text
        self.assertIn('Username is required', error_message)

    def test_empty_password(self):
        driver = self.driver
        driver.find_element(By.ID, 'username').send_keys('validuser')
        driver.find_element(By.ID, 'password').send_keys('')
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, 'error-message').text
        self.assertIn('Password is required', error_message)

    def test_nonexistent_username(self):
        driver = self.driver
        driver.find_element(By.ID, 'username').send_keys('nonexistentuser')
        driver.find_element(By.ID, 'password').send_keys('somepassword')
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, 'error-message').text
        self.assertIn('User does not exist', error_message)

    def test_weak_password(self):
        driver = self.driver
        driver.find_element(By.ID, 'username').send_keys('validuser')
        driver.find_element(By.ID, 'password').send_keys('123')
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, 'error-message').text
        self.assertIn('Password does not meet strength requirements', error_message)

    def test_excessive_length_credentials(self):
        driver = self.driver
        long_username = 'u' * 256
        long_password = 'p' * 256
        driver.find_element(By.ID, 'username').send_keys(long_username)
        driver.find_element(By.ID, 'password').send_keys(long_password)
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, 'error-message').text
        self.assertIn('Username or password is too long', error_message)

    def test_incorrect_case_username(self):
        driver = self.driver
        driver.find_element(By.ID, 'username').send_keys('VALIDUSER')
        driver.find_element(By.ID, 'password').send_keys('validpassword')
        driver.find_element(By.ID, 'login-button').click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, 'error-message').text
        self.assertIn('Invalid username or password', error_message)

    def test_existing_username(self):
        driver = self.driver
        driver.get('http://example.com/register')  # Replace with your registration URL
        time.sleep(2)
        driver.find_element(By.ID, 'username').send_keys('existinguser')
        driver.find_element(By.ID, 'password').send_keys('newpassword')
        driver.find_element(By.ID, 'register-button').click()
        time.sleep(2)
        error_message = driver.find_element(By.ID, 'error-message').text
        self.assertIn('Username already exists', error_message)

if __name__ == '__main__':
    unittest.main()
