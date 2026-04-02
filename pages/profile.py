import logging
import time
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException, NoSuchElementException

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# Upload profile picture from Camera
class ProfileActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def update_profile_picture_from_camera(self):
        try:
            profile_image_icon = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Open navigation menu')))
            profile_image_icon.click()

            view_profile_option = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'View profile')))
            view_profile_option.click()

            profile_picture_edit_icon = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Edit')))
            profile_picture_edit_icon.click()

            from_camera_option = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Take photo')))
            from_camera_option.click()
    
            # permission = self.wait.until(EC.element_to_be_clickable(
            #     (AppiumBy.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button"))
            # )
            # if permission:
            #     permission.click()
            #     logging.info("Permission popup handled.")
            # else:
            #     logging.info("Permission popup not shown.")

            shutter_button = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Shutter')))
            shutter_button.click()
            time.sleep(1)
            
            done_button = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Done')))
            done_button.click()
            time.sleep(1)

            logging.info("Profile picture updated successfully from camera.")
            
        except (TimeoutException, NoSuchElementException, Exception) as e:
            logging.error(f"Failed to update profile picture: {str(e)}")
            raise

    def update_profile_picture_from_gallery(self):
        wait = WebDriverWait(self.driver, 10)

        try:
            profile_picture_edit_icon = wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Edit')))
            profile_picture_edit_icon.click()

            from_gallery_option = wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Choose photo from gallery')))
            from_gallery_option.click()
            
            image_elements = self.driver.find_elements(AppiumBy.ID,
                'com.google.android.providers.media.module:id/icon_thumbnail')

            if image_elements:
                select_img = image_elements[0]
                select_img.click()
                time.sleep(0.5)
                rotate = wait.until(EC.element_to_be_clickable(
                    (AppiumBy.ACCESSIBILITY_ID, 'Rotate')))
                rotate.click()
                
                flip = wait.until(EC.element_to_be_clickable(
                    (AppiumBy.ACCESSIBILITY_ID, 'Flip')))
                flip.click()
                flip_h = wait.until(EC.element_to_be_clickable(
                    (AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.figure1.development:id/content"])[1]')))
                flip_h.click()
                
                flip = wait.until(EC.element_to_be_clickable(
                    (AppiumBy.ACCESSIBILITY_ID, 'Flip')))
                flip.click()
                flip_v = wait.until(EC.element_to_be_clickable(
                    (AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.figure1.development:id/content"])[2]')))
                flip_v.click()
                
                crop = wait.until(EC.element_to_be_clickable(
                    (AppiumBy.ID, 'com.figure1.development:id/crop_image_menu_crop')))
                crop.click()
                time.sleep(1)
                
                image_displayed = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView')))
                if image_displayed:
                    logging.info("Image preview displayed.")
                else:
                    logging.warning("Image preview not found.")
            else:
                self.driver.press_keycode(4)
                logging.info("Image not found, skipping selection and crop.")

            logging.info("Profile picture selection from gallery verified successfully.")

        except (NoSuchElementException, TimeoutException, Exception) as e:
            logging.error(f"Failed to update profile picture from gallery: {str(e)}")
            raise


    def navigate_and_search_user(self, username="PAnkk"):
        try:
            time.sleep(0.5)
            followers = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'View followers')))
            followers.click()
            time.sleep(0.5)
            following = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Following')))
            following.click()
            time.sleep(0.5)
            search_members = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'Search members')))
            search_members.click()
            time.sleep(1)
            time.sleep(0.5)
            search_box = self.wait.until(EC.presence_of_element_located(
                (AppiumBy.ACCESSIBILITY_ID, 'Search')))
            search_box.click()
            search_box.send_keys(username)
            time.sleep(1)
            self.driver.press_keycode(66)
            time.sleep(0.5)
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
            
            following_again = self.wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, 'View following'))) 
            following_again.click()
            time.sleep(1)

            self.driver.press_keycode(4)
            time.sleep(0.5)

            logging.info("User navigation and search flow completed successfully.")

        except (TimeoutException, NoSuchElementException, Exception) as e:
            logging.error(f"Error occurred in navigate_and_search_user: {e}")
            traceback.print_exc()
        
            
    def edit_profile_details(self):
        try:
            edit_profile_btn = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Edit profile')))
            edit_profile_btn.click()
            time.sleep(0.5)

            edit_details_btn = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Edit details')))
            edit_details_btn.click()
            time.sleep(1)

            profession_specialty = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Edit profession')))
            profession_specialty.click()
            time.sleep(0.5)

            location_field = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Physician Assistant')))
            location_field.click()
            time.sleep(1)

            primary_specialty = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Edit primary specialty')))
            primary_specialty.click()
            time.sleep(0.5)

            case_title_input = self.wait.until(EC.presence_of_element_located((
                AppiumBy.ACCESSIBILITY_ID, "Search")))
            case_title_input.click()
            case_title_input.send_keys("Family")
            self.driver.press_keycode(66)
            time.sleep(0.5)

            # family_add = self.wait.until(EC.element_to_be_clickable((
            #     AppiumBy.XPATH, '//android.widget.TextView[@text="Family Medicine"]')))
            # family_add.click()
            # time.sleep(0.5)
            self.driver.press_keycode(4)
            time.sleep(0.5)

            self.driver.press_keycode(4)
            time.sleep(0.5)

            About = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Edit where do you practice'
            )))
            About.click()

            search = self.wait.until(EC.presence_of_element_located((
                AppiumBy.ACCESSIBILITY_ID, 'Where do you practice input'
            )))
            search.click()
            search.clear()
            search.send_keys("This is a test practice")

            Save = self.wait.until(EC.presence_of_element_located((
                AppiumBy.ACCESSIBILITY_ID, 'Save'
            )))
            Save.click()
            time.sleep(0.5)

            Screen = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Profile updated'
            )))
            Screen.click()
            time.sleep(0.5)

            hospital = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Edit practicing hospital'
            )))
            hospital.click()

            search = self.wait.until(EC.presence_of_element_located((
                AppiumBy.ACCESSIBILITY_ID, 'Practicing hospital input'
            )))
            search.click()
            search.clear()
            search.send_keys("This is a test hospital")

            Save = self.wait.until(EC.presence_of_element_located((
                AppiumBy.ACCESSIBILITY_ID, 'Save'
            )))
            Save.click()
            time.sleep(0.5)

            Screen = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Profile updated'
            )))
            Screen.click()
            time.sleep(0.5)

            bio = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Edit bio'
            )))
            bio.click()

            search = self.wait.until(EC.presence_of_element_located((
                AppiumBy.ACCESSIBILITY_ID, 'Bio input'
            )))
            search.click()
            search.clear()
            search.send_keys("This is a test bio")

            Save = self.wait.until(EC.presence_of_element_located((
                AppiumBy.ACCESSIBILITY_ID, 'Save'
            )))
            Save.click()

            Screen = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Profile updated'
            )))
            Screen.click()

            self.driver.press_keycode(4)
            time.sleep(0.5)

            logging.info("Edit profile details flow completed successfully.")

        except (TimeoutException, NoSuchElementException, Exception):
            logging.error("Error in edit_profile_details:")
            logging.error(traceback.format_exc())


    def invite_to_network(self):
        try:
            invite_button = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Invite to my network')))
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

            logging.info("Invite to network functionality verified successfully.")

        except (TimeoutException, NoSuchElementException, Exception):
            logging.error("Error in invite_to_network:")
            logging.error(traceback.format_exc())
            

    def add_more_interests(self, speciality="Ca"):
        try:
            interest_section = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'View my interests')))  
            interest_section.click()
            time.sleep(0.5)

            add_more_button = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Add more interests')))
            add_more_button.click()
            time.sleep(0.5)

            text_field = self.wait.until(EC.presence_of_element_located((
                AppiumBy.CLASS_NAME, "android.widget.EditText")))
            text_field.click()
            text_field.clear()
            text_field.send_keys(speciality)
            self.driver.press_keycode(66)
            time.sleep(1)

            interest_result = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Cancer Genetics')))
            interest_result.click()
            time.sleep(0.5)

            next_button = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Next')))
            next_button.click()
            time.sleep(0.5)

            self.driver.implicitly_wait(0)
            try:
                short_wait = WebDriverWait(self.driver, 1)
                Press = short_wait.until(
                    EC.presence_of_element_located(
                        (AppiumBy.XPATH,'//android.widget.TextView[@text=" Cancer Genetics  x "]')))

                if Press.is_displayed():
                    Press.click()
            except TimeoutException:
                logging.error("Interest not found.")
            
            Save = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Save')))
            Save.click()
            # time.sleep(0.5)
            # self.driver.press_keycode(4)
            logging.info("Add more interests functionality verified successfully.")
            
        except Exception:
            logging.error("Error in add_more_interests function:")
            logging.error(traceback.format_exc())
            
            
    def add_work_experience(self):
        try:
            about_section = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'About tab')))
            about_section.click()

            # Scroll to end
            self.wait.until(lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(5)'
            ))
            time.sleep(1.5)

            add_experience = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Edit experience')))
            add_experience.click()

            add_work = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Add experience')))
            add_work.click()

            position_field = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Position')))
            position_field.send_keys("Test")

            company_field = self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Company')))
            company_field.send_keys("Test1")
            self.driver.press_keycode(66)

            self.wait.until(lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("Start year")')).click()

            self.wait.until(lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true))'
                '.scrollIntoView(new UiSelector().text("1929"))')).click()

            self.wait.until(lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().text("End year")')).click()

            self.wait.until(lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true))'
                '.scrollIntoView(new UiSelector().text("1935"))')).click()

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Save'))).click()
            
            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Profile updated'))).click()
            
            # Edit & Delete experience
            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Edit experience'))).click()

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Delete'))).click()

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ID, 'android:id/button2'))).click()

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Profile updated'))).click()
            
            self.driver.press_keycode(4)
            logging.info("Work experience section verified successfully.")

        except Exception as e:
            logging.error(f"An error occurred in add_work_experience: {e}")
            
            
    def add_education(self):
        try:
            # Scroll to end
            self.wait.until(lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(5)'
            ))
            time.sleep(1.5)

            # Edit education
            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Edit education'))).click()

            # Add education
            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Add education'))).click()

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'School name'))).send_keys("Edu Test")

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Degree'))).send_keys("Test002")
            self.driver.press_keycode(66)

            self.wait.until(lambda d: d.find_element(
                AppiumBy.ACCESSIBILITY_ID, 'Start year')).click()

            self.wait.until(lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true))'
                '.scrollIntoView(new UiSelector().text("1945"))')).click()

            self.wait.until(lambda d: d.find_element(
                AppiumBy.ACCESSIBILITY_ID, 'End year')).click()

            self.wait.until(lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true))'
                '.scrollIntoView(new UiSelector().text("1948"))')).click()

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Save'))).click()

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Profile updated'))).click()
            
            # Edit & Delete education
            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Edit education'))).click()

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Delete'))).click()

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ID, 'android:id/button2'))).click()

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Profile updated'))).click()
            
            self.driver.press_keycode(4)
            logging.info("Education section verified successfully.")

        except Exception as e:
            logging.error(f"An error occurred in add_education: {e}")
            
            
    def add_affiliations(self):
        try:
            # Scroll to end
            self.wait.until(lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true)).scrollToEnd(5)'
            ))
            time.sleep(1.5)

            # Edit affiliations
            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID,
                'Edit affiliations and memberships'
            ))).click()

            # Add affiliation
            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID,
                'Add affiliations and memberships'
            ))).click()

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID,
                'Affiliations and memberships'
            ))).send_keys("Af Testing")
            self.driver.press_keycode(66)

            self.wait.until(lambda d: d.find_element(
                AppiumBy.ACCESSIBILITY_ID, 'Start year')).click()

            self.wait.until(lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true))'
                '.scrollIntoView(new UiSelector().text("1927"))')).click()

            self.wait.until(lambda d: d.find_element(
                AppiumBy.ACCESSIBILITY_ID, 'End year')).click()

            self.wait.until(lambda d: d.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiScrollable(new UiSelector().scrollable(true))'
                '.scrollIntoView(new UiSelector().text("1936"))')).click()

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Save'))).click()

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Profile updated'))).click()
        
            # Edit & Delete affiliation

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID,
                'Edit affiliations and memberships'))).click()

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Delete'))).click()

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ID, 'android:id/button2'))).click()

            self.wait.until(EC.element_to_be_clickable((
                AppiumBy.ACCESSIBILITY_ID, 'Profile updated'))).click()
            
            time.sleep(1.5)
            self.driver.press_keycode(4)
            time.sleep(0.7)
            self.driver.press_keycode(4)
            time.sleep(1)
            logging.info("Affiliations section verified successfully.")

        except Exception as e:
            logging.error(f"An error occurred in add_affiliations: {e}")

