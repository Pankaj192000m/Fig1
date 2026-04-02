import time
import pytest
from pages.signup import Signuppage
from pages.login import LoginActions

@pytest.mark.signup_smoke
@pytest.mark.skip(reason="Skipping signup for this run")
def test_signup_only_flow(driver):
    signup = Signuppage(driver)
    signup.onetrust_accept_cookies()
    signup.signupUSWithoutNPI()