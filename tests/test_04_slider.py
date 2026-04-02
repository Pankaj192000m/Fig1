import pytest
from pages.slider import SliderActions

@pytest.mark.slider_smoke
def test_slider(driver):
    profile = SliderActions(driver)
    profile.update_saved()
    profile.draft_module()
    profile.My_network()
    profile.invite_to_network()
    profile.help_feedback()
    profile.manage_my_account()   