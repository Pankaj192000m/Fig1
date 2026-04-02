import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from core.base_page import BasePage

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
class LoginActions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.long_wait = WebDriverWait(driver, 20)

    def onetrust_accept_cookies(self):
        try:
            accept_cookies_button = self.long_wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, 'com.figure1.development:id/btn_accept_cookies'))
            )
            accept_cookies_button.click()
            logging.info("OneTrust cookies accepted.")
        except TimeoutException:
            logging.info("OneTrust cookie banner not found or already accepted.")

    def test_perform_login(self):
        try:
            login_button = self.long_wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Log in')))
            login_button.click()

            username_field = self.long_wait.until(EC.presence_of_element_located((
                AppiumBy.ACCESSIBILITY_ID, 'Email address'
            )))
            username_field.clear()
            username_field.send_keys("RSha")
            logging.info("Correct username entered.")

            password_field = self.long_wait.until(EC.presence_of_element_located((
                AppiumBy.ACCESSIBILITY_ID, 'Password'
            )))
            password_field.clear()
            password_field.send_keys("Primo@123")
            logging.info("Correct password entered.")

            login_button = self.long_wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Sign in'
            )))
            login_button.click()
            logging.info("Login action performed successfully.")
            time.sleep(5)

        except Exception as e:
            logging.info(f"Unexpected error during login: {e}")

    def dismiss_notification_prompt(self):
        wait = WebDriverWait(self.driver, 15)  

        try:
            logging.info("Waiting for notification prompt (if any)...")
            notification = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="Not now"]')))
            notification.click()
            logging.info("Notification prompt dismissed.")
            time.sleep(2)
        except TimeoutException:
            logging.info("Notification prompt already dismissed.")
        except Exception as e:
            logging.error(f"Notification prompt not found or already dismissed. ({e})")

    def validate_login(self):
        try:
            profile_icon = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Open navigation menu')))
            logging.info("User logged in successfully and dashboard is displayed")
            return True
        except TimeoutException:
            logging.error("User Login failed: dashboard is not displayed.")
            return False