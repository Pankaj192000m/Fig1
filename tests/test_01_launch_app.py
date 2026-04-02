import pytest
from pages.Launchapp import DeviceNavigation

@pytest.mark.smoke
def test_app_launch(driver):
    nav = DeviceNavigation(driver)
    nav.go_to_home_screen()
    nav.launch_figure1_app()
