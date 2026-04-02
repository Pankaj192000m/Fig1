import os
import pytest
import time
from core.base import start_emulator,install_app_once, get_driver

# Screenshot on failure hook
@pytest.fixture(scope="session")
def driver():
    start_emulator()
    install_app_once()           #Install and Uninstall app before starting driver
    drv = get_driver()
    print("Driver session started")
    yield drv
    drv.quit()
    print("Driver session closed")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    # Only after test call (not setup/teardown)
    if result.when == 'call' and result.failed:
        driver = item.funcargs.get('driver', None)
        if driver:
            # Screenshots folder
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            # File name with timestamp to avoid overwrite
            file_name = f"{item.name}_{int(round(time.time() * 1000))}.png"
            file_path = os.path.join(screenshot_dir, file_name)

            # Save screenshot
            driver.save_screenshot(file_path)

            # Attach to pytest-html report
            extra = getattr(result, 'extra', [])
            if file_path and 'pytest_html' in globals():
                html = f'<div><img src="screenshots/{file_name}" width="300"/></div>'
                extra.append(pytest_html.extras.html(html))
            result.extra = extra


# Register pytest-html plugin
def pytest_configure(config):
    global pytest_html
    pytest_html = config.pluginmanager.getplugin('html')
