import os
import time
from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


EMULATOR_NAME = "Pixel_4_API_30"

def start_emulator():
    print("Checking if emulator is running...")
    devices = os.popen("adb devices").read()
    if "emulator-5554" not in devices:
        print("Starting emulator...")
        os.system(f"emulator -avd {EMULATOR_NAME} -no-snapshot-load")
        time.sleep(20)

PACKAGE_NAME = "com.figure1.development"

def install_app_once():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    apk_path = os.path.join(base_dir, "..", "apks", "app-release-feature-testid.apk")

    # uninstall old app (safe)
    os.system(f"adb uninstall {PACKAGE_NAME}")

    # install fresh APK
    os.system(f'adb install "{apk_path}"')

def get_driver() -> webdriver.Remote:
    cap: Dict[str, Any] = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "automationName": "UIAutomator2",
        "appPackage": PACKAGE_NAME,
        "autoLaunch": False, 
        #"noReset": True,                 #----Comment for reset app state every time
        "autoGrantPermissions": True,
    }
    url = 'http://127.0.0.1:4723'
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    driver.implicitly_wait(10)
    return driver
