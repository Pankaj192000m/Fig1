import time
from numpy import size
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver, implicit_wait=5, explicit_wait=5):
        self.driver = driver
        self.driver.implicitly_wait(implicit_wait)   
        self.wait = WebDriverWait(driver, explicit_wait)

    # ---------- BASIC ACTIONS ----------

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.wait_for_presence(locator)
        self.wait_for_clickable(locator).click()

    def type(self, locator, text):
        element = self.wait_for_presence(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.wait_for_presence(locator).text

    def press_back(self, times=1):
        for _ in range(times):
            self.driver.press_keycode(4)
            time.sleep(0.5)

    def sleep(self, seconds=1):
        time.sleep(seconds)

    def swipe_up(self, duration=500):
        """Swipe up the screen."""
        size = self.driver.get_window_size()
        start_x = size['width'] * 0.5
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.2
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)

    def swipe_until_visible(self, locator, max_swipes=5, duration=500):
        for _ in range(max_swipes):
            try:
                return self.wait_for_presence(locator)
            except TimeoutException:
                self.swipe_up(duration)

    def swipe_down(self, duration=150):
        size = self.driver.get_window_size()
        start_x = int(size['width'] * 0.5)
        start_y = int(size['height'] * 0.6)   # Start from middle
        end_y   = int(size['height'] * 0.85)  # Move downward
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)
