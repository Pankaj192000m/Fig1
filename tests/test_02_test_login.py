import time
import pytest
from pages.signup import Signuppage
from pages.login import LoginActions

@pytest.mark.login_smoke
def test_login_only_flow(driver):
    login = LoginActions(driver)
    login.onetrust_accept_cookies()
    login.test_perform_login()
    login.dismiss_notification_prompt()
    login.validate_login()
    time.sleep(2)
