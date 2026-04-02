import logging
from socket import timeout
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.base_page import BasePage


class Signuppage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_back(self):
        go_back_btn = (AppiumBy.ACCESSIBILITY_ID, "Go back")
        self.click(go_back_btn)

    def onetrust_accept_cookies(self):
        try:
            accept_cookies_button = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.ID, 'com.figure1.development:id/btn_accept_cookies'))
            )
            accept_cookies_button.click()
            logging.info("OneTrust cookies accepted.")
        except TimeoutException:
            logging.info("OneTrust cookie banner not found or already accepted.")

    def signupUSWithoutNPI(self):
        try:
            signup_button = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Sign up')))
            signup_button.click()

            email_field = self.wait.until(EC.presence_of_element_located((
                AppiumBy.ACCESSIBILITY_ID, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[1]'
            )))
            email_field.clear()
            email_field.send_keys("RSha")

            password_field = self.wait.until(EC.presence_of_element_located((
                AppiumBy.ACCESSIBILITY_ID, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText[2]'
            )))
            password_field.clear()
            password_field.send_keys("Primo@123")

            login_button = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Sign in'
            )))
            login_button.click()
            logging.info("Login action performed successfully.")
            time.sleep(5)

        except Exception as e:
            logging.info(f"Unexpected error during login: {e}")