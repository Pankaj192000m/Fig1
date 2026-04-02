import time
import logging
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from numpy import size
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class DeviceNavigation:
    def __init__(self, driver: WebDriver):
        """Initialize with the Appium WebDriver instance."""
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def go_to_home_screen(self) -> None:
        """Navigate to the Android home screen."""
        self.driver.press_keycode(3)  
        time.sleep(1)
        # self.driver.terminate_app("com.figure1.development")  #("com.figure1.android")--- Use this for production app

    def launch_figure1_app(self) -> None:
        """Launch the Figure1 app"""
        try:
            self.driver.activate_app("com.figure1.development")
            logging.info("Figure1 app launched successfully.")
        except NoSuchElementException:
            raise AssertionError("Figure1 app icon not found on the device.")
