import pytest
from pages.home_feed import HomeFeedActions

@pytest.mark.home_smoke
def test_home_feed_actions(driver):
    home = HomeFeedActions(driver)
    home.explore_tab()
    home.notification_tab()
    home.case_tab()
    home.post_tab()
    home.community()
    home.search()
    # home.my_feed()