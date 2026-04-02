import time
import logging
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from core.base_page import BasePage

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

class SliderActions(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        super().__init__(driver)

    def swipe_up(self, duration=500):
        """Helper to swipe up the screen."""
        size = self.driver.get_window_size()
        start_x = size['width'] * 0.5
        start_y = size['height'] * 0.8
        end_y = size['height'] * 0.2
        self.driver.swipe(start_x, start_y, start_x, end_y, duration)

    def update_saved(self):
        try:
            time.sleep(2)
            self.driver.implicitly_wait(0)

            save_case = (AppiumBy.ACCESSIBILITY_ID, 'Save case')

            found = self.swipe_until_visible(save_case) 

            if not found:
                logging.warning("Element not found after maximum swipes. Skipping update_saved.")
            
                my_feed = (AppiumBy.ACCESSIBILITY_ID, "My Feed")
                self.click(my_feed)
                time.sleep(2)
                return

            self.click(save_case)

            profile_image_icon = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Open navigation menu')))
            profile_image_icon.click()
            time.sleep(0.5)

            saved_tab = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Saved posts')))
            saved_tab.click()
            time.sleep(1)

            elements = self.driver.find_elements(
                AppiumBy.ACCESSIBILITY_ID,"Saved post")

            if elements:
                first_item = elements[0]
                self.driver.execute_script("mobile: swipeGesture", {
                    "elementId": first_item.id,
                    "direction": "left",
                    "percent": 0.9
                })
                delete_saved = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID,
                'Remove saved post')))
                delete_saved.click()
            else:
                logging.info("No saved items found. Skipping swipe.")
  
            self.driver.press_keycode(4)
            time.sleep(1)
            logging.info("Saved module updated successfully.")

        except (TimeoutException, NoSuchElementException, Exception) as e:
            logging.error(f"Failed to update saved: {str(e)}")
            return  
        
    def draft_module(self):
        try:
            time.sleep(1.5)
            profile_image_icon = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Open navigation menu'
            )))
            profile_image_icon.click()
            time.sleep(0.5)

            draft_tab = self.wait.until(
                EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Drafts'))
            )
            draft_tab.click()
            
            time.sleep(1)
            self.driver.press_keycode(4)
            logging.info("Drafts accessed successfully.")
            
        except (TimeoutException, NoSuchElementException, Exception) as e:
            logging.error(f"Failed to access drafts: {str(e)}")
            raise

        
    def My_network(self, username="PAnkk"):
        try:
            # Profile image icon
            profile_image_icon = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Open navigation menu'
            )))
            profile_image_icon.click()
            time.sleep(0.5)

            # 'My network'
            networks = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'My network'
            )))
            networks.click()

            following = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Following')))
            following.click()
            time.sleep(1)

            search_members = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Search members')))
            search_members.click()
            time.sleep(1)

            search_box = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, 'Search')))
            search_box.click()
            search_box.send_keys(username)
            self.driver.press_keycode(66)
            
            elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((AppiumBy.XPATH, '//android.widget.TextView[@text="PAnkk"]')))

            if elements:
                logging.info("Account is visible.")
            else:
                logging.info("Account not visible.")

            cross = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Clear search')))
            cross.click()
            time.sleep(2)

            case_tab = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Search cases')))
            case_tab.click()
            time.sleep(1)

            case_search = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, 'Search')))
            case_search.click()
            case_search.send_keys("cold")
            self.driver.press_keycode(66)
            
            cross = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Clear search')))
            cross.click()

            self.driver.press_keycode(4)
            time.sleep(0.5)
            self.driver.press_keycode(4)
            
            logging.info("My_network navigation and search completed successfully.")

        except Exception as e:
            logging.error(f"Error occurred in My_network: {e}")


    def invite_to_network(self):
        try:
            profile_image_icon = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Open navigation menu'
            )))
            profile_image_icon.click()
            time.sleep(0.5)

            invite_button = self.wait.until(EC.presence_of_element_located((
                AppiumBy.ACCESSIBILITY_ID, 'Invite colleagues')))
            invite_button.click()
            time.sleep(0.5)

            copy_link_button = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Copy invitation link')))
            copy_link_button.click()
            time.sleep(0.5)

            try:
                popup = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(
                        (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Invitation link copied"]/android.view.ViewGroup/android.view.ViewGroup')
                    )
                )
                if popup.is_displayed():
                    logging.info("Popup appeared: Invitation link copied")
            except TimeoutException:
                logging.error("Popup did not appear: 'Invitation link copied' not found within timeout")

            tap1 = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Invitation link copied"]/android.view.ViewGroup/android.view.ViewGroup')))
            tap1.click()
            time.sleep(0.5)

            share_link_button = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Share link via..., Share this link with your colleagues')))
            share_link_button.click()
            time.sleep(0.5)

            for _ in range(2):  
                self.driver.press_keycode(4)

            logging.info("invite_to_network checked successfully")

        except (TimeoutException, NoSuchElementException, Exception):
            logging.error("Error in invite_to_network:")
            logging.error(traceback.format_exc())

        
    def help_feedback(self):
        try:
            help_menu = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Help and feedback')))
            help_menu.click()

            # view_faq = self.wait.until(EC.element_to_be_clickable(
            #     (AppiumBy.ACCESSIBILITY_ID, 'View FAQs')))
            # view_faq.click()

            # close = self.wait.until(EC.element_to_be_clickable(
            #     (AppiumBy.ACCESSIBILITY_ID, 'Close tab')))
            # close.click()

            # contact_us = self.wait.until(EC.element_to_be_clickable(
            #     (AppiumBy.ACCESSIBILITY_ID, 'Contact Support')))
            # contact_us.click()
            # self.driver.press_keycode(4)

            # give_feedback = self.wait.until(EC.element_to_be_clickable(
            #     (AppiumBy.ACCESSIBILITY_ID, 'Give feedback')))
            # give_feedback.click()
            # self.driver.press_keycode(4)

            # Privacy_policy = self.wait.until(EC.element_to_be_clickable(
            #     (AppiumBy.ACCESSIBILITY_ID, 'Privacy Policy')))
            # Privacy_policy.click()
            # self.driver.press_keycode(4)

            # term_and_conditions = self.wait.until(EC.element_to_be_clickable(
            #     (AppiumBy.ACCESSIBILITY_ID, 'Terms and Conditions')))
            # term_and_conditions.click()
            # self.driver.press_keycode(4)

            # claim_cme = self.wait.until(EC.element_to_be_clickable(
            #     (AppiumBy.ACCESSIBILITY_ID, 'Claim CME credits')))
            # claim_cme.click()

            back_button = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID,'Go back')))
            back_button.click()

            logging.info("Help & Feedback section accessed successfully.")

        except Exception:
            logging.error("Failed to access Help & Feedback section.")
            traceback.print_exc()    

    def manage_my_account(self):
        try:
            #--------------Un comment if reset link needs to be tested-------------------
            # profile_image_icon = self.wait.until(EC.element_to_be_clickable((
            #     AppiumBy.ACCESSIBILITY_ID, 'Open navigation menu'
            # )))
            # profile_image_icon.click()

            # account_settings = self.wait.until(EC.element_to_be_clickable(
            #     (AppiumBy.ACCESSIBILITY_ID, 'Account settings')))
            # account_settings.click()

            # manage_intrests = self.wait.until(EC.element_to_be_clickable(
            #     (AppiumBy.ACCESSIBILITY_ID, 'Manage your interests, This helps us personalize cases in the ‘For you’ feed')))
            # manage_intrests.click()
            # self.driver.press_keycode(4)

            # manage_account = self.wait.until(EC.element_to_be_clickable(
            #     (AppiumBy.ACCESSIBILITY_ID, 'Manage my account')))
            # manage_account.click()

            # reset_password = self.wait.until(EC.element_to_be_clickable(
            #     (AppiumBy.ACCESSIBILITY_ID, 'Reset my password')))
            # reset_password.click()

            # send_link = self.wait.until(EC.element_to_be_clickable(
            #     (AppiumBy.ACCESSIBILITY_ID, 'Send reset link')))
            # send_link.click()
            
            # done_button = self.wait.until(EC.element_to_be_clickable(
            #     (AppiumBy.ACCESSIBILITY_ID, 'Done')))
            # done_button.click()

            profile_image_icon = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Open navigation menu'
            )))
            profile_image_icon.click()

            account_settings = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Account settings')))
            account_settings.click()

            manage_account = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Manage my account')))
            manage_account.click()

            Update_email = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Update email / username')))
            Update_email.click()
            time.sleep(0.5)
            self.driver.press_keycode(4)

            Update_privacy = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Update privacy settings')))
            Update_privacy.click()

            self.driver.press_keycode(4)
            time.sleep(0.7)
            self.driver.press_keycode(4)
            time.sleep(0.7)
            self.driver.press_keycode(4)
            time.sleep(1)

            logging.info("Account settings managed successfully.")

        except Exception:
            logging.error("Failed to manage account settings.")
            traceback.print_exc()