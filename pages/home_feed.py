import logging
from socket import timeout
import time
from appium.webdriver.common.appiumby import AppiumBy
from core.base_page import BasePage


class HomeFeedActions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_back(self):
        go_back_btn = (AppiumBy.ACCESSIBILITY_ID, "Go back")
        self.click(go_back_btn)
        
    def explore_tab(self):
        try:
            self.driver.press_keycode(4)
            time.sleep(1)
            # ================== OPEN EXPLORE TAB ==================
            explore_tab = (
                AppiumBy.ACCESSIBILITY_ID,
                "Explore"
            )
            self.wait_for_presence(explore_tab)
            self.click(explore_tab)
            time.sleep(0.7)
            self.click(explore_tab)
            
            # ================== NEWEST SECTION ==================
            newest_view_all = (
                AppiumBy.ACCESSIBILITY_ID,
                "Newest view all"
            )
            self.click(newest_view_all)

            back_button = (
                AppiumBy.ACCESSIBILITY_ID,
                "Go back"
            )
            self.click(back_button)

            # ================== TRENDING NOW SECTION ==================
            trending_view_all = (
                AppiumBy.ACCESSIBILITY_ID,
                "Trending now view all"
            )
            self.click(trending_view_all)

            back_button = (
                AppiumBy.ACCESSIBILITY_ID,
                "Go back"
            )
            self.click(back_button)

            # ================== ANESTHESIOLOGY SECTION ==================
            # Anesthesiology_view_all = (
            #     AppiumBy.ACCESSIBILITY_ID,
            #     "Anesthesiology view all"
            # )
            # self.click(Anesthesiology_view_all)

            # back_button = (
            #     AppiumBy.ACCESSIBILITY_ID,
            #     "Go back"
            # )
            # self.click(back_button)

            # # ================== Cardiology SECTION ==================
            # Cardiology_view_all = (
            #     AppiumBy.ACCESSIBILITY_ID,
            #     "Cardiology view all"
            # )
            # self.swipe_until_visible(Cardiology_view_all)
            # self.click(Cardiology_view_all)

            # back_button = (
            #     AppiumBy.ACCESSIBILITY_ID,
            #     "Go back"
            # )
            # self.click(back_button)

            # ================== Quizzes SECTION ==================
            Quizzes_view_all = (
                AppiumBy.ACCESSIBILITY_ID,
                "Quizzes+ view all"
            )
            self.swipe_until_visible(Quizzes_view_all, max_swipes=8, duration=100)
            self.click(Quizzes_view_all)

            back_button = (
                AppiumBy.ACCESSIBILITY_ID,
                "Go back"
            )
            self.click(back_button)

            logging.info("Explore tab sections executed successfully.")

        except Exception as e:
            logging.error(f"Error occurred in explore_tab: {e}")
            raise


    def notification_tab(self):
        try:
            # ================== OPEN NOTIFICATION TAB ==================
            notification_tab = (
                AppiumBy.ACCESSIBILITY_ID,
                "Notifications"
            )
            self.click(notification_tab)

            mark_all_read = (AppiumBy.XPATH, "//android.widget.TextView[@text='Mark all as read']")
            Done = (AppiumBy.ACCESSIBILITY_ID, "Done")
            self.click(mark_all_read)
            try:
                self.click(Done)
            except Exception:
                logging.info("Notifications already marked as read.")
            logging.info("Notification tab actions executed successfully.")

        except Exception as e:
            logging.error(f"Error occurred in notification_tab: {e}")
            raise


    def case_tab(self):
        try:
            # ================== OPEN POST TAB ==================
            post_tab = (
                AppiumBy.ACCESSIBILITY_ID,
                "Post"
            )
            self.click(post_tab)

            clinical_case = (
                AppiumBy.ACCESSIBILITY_ID,
                "Create clinical case"
            )
            self.click(clinical_case)

            select_one = (
                AppiumBy.ACCESSIBILITY_ID,
                "Choose audience"
            )
            self.click(select_one)

            select_group = (
                AppiumBy.ACCESSIBILITY_ID,
                "Share with Figure 1 public"
            )
            self.click(select_group)

            # add_photos = (
            #     AppiumBy.ACCESSIBILITY_ID,
            #     "Add media"
            # )
            # self.click(add_photos)

            # from_camera_option = (AppiumBy.ACCESSIBILITY_ID, "From Camera")
            # self.click(from_camera_option)
    
            # permission = self.driver.find_elements(
            #     AppiumBy.ID,"com.android.permissioncontroller:id/permission_allow_foreground_only_button")

            # if permission:
            #     permission[0].click()
            #     logging.info("Permission popup handled.")
            # else:
            #     logging.info("Permission popup not shown.")

            # shutter_button = (
            #     AppiumBy.ACCESSIBILITY_ID, 'Shutter'
            # )
            # shutter_button.click()

            add_title = (
                AppiumBy.ACCESSIBILITY_ID,
                "Case title"
            )
            self.click(add_title)
            self.type(add_title, "Testing title")
            
            add_des = (
                AppiumBy.ACCESSIBILITY_ID,
                "Case description"
            )
            self.click(add_des)
            self.type(add_des, "Testing Description")

            self.press_back()

            tags_common = (
                AppiumBy.ACCESSIBILITY_ID,
                "caseLabel-ac7dbc06-3633-4b97-bb31-3f5d431be326"
            )
            self.click(tags_common)

            tags_rare = (
                AppiumBy.ACCESSIBILITY_ID,
                "caseLabel-dc311e7a-3d7a-45fc-9172-221a42da5a05"
            )
            self.click(tags_rare)

            resolve = (
                AppiumBy.ACCESSIBILITY_ID,
                "Mark case as resolved"
            )
            self.click(resolve)

            exit_dia = (
                AppiumBy.ACCESSIBILITY_ID,
                "Exit diagnosis"
            )
            self.click(exit_dia)
            
            Unresolved = (
                AppiumBy.ACCESSIBILITY_ID,
                "Mark case as unresolved"
            )
            self.click(Unresolved)

            save = (
                AppiumBy.ACCESSIBILITY_ID,
                "Save"
            )
            self.click(save)

            add_specialities = (
                AppiumBy.ACCESSIBILITY_ID,
                "Add specialty"
            )
            self.swipe_until_visible(add_specialities)
            self.click(add_specialities)

            abdominal = (
                AppiumBy.ACCESSIBILITY_ID,
                "CASE_SPECIALTY_SEARCH_LIST_ITEM_0"
            )
            self.click(abdominal)

            save = (
                AppiumBy.ACCESSIBILITY_ID,
                "Save"
            )
            self.click(save)

            save_as_draft = (
                AppiumBy.ACCESSIBILITY_ID,
                "Update draft")
            self.swipe_until_visible(save_as_draft)
            self.click(save_as_draft)

            draft_popup = (AppiumBy.ACCESSIBILITY_ID, "Draft Saved")
            self.click(draft_popup)

            cross_button = (
                AppiumBy.ACCESSIBILITY_ID,
                "Go back"
            )
            self.click(cross_button)

            draft_popup = (AppiumBy.ACCESSIBILITY_ID, "Draft Saved")
            try:
                element = self.wait_for_presence(draft_popup)  
                element.click()
            except:
                logging.error("Draft not saved: popup did not appear.")
            logging.info("Case share executed successfully.")

        except Exception as e:
            logging.error(f"Error occurred in case_tab: {e}")
            raise

    def post_tab(self):
        try:
            # ================== OPEN POST TAB ==================
            post_tab = (
                AppiumBy.ACCESSIBILITY_ID,
                "Post"
            )
            self.click(post_tab)

            post = (
                AppiumBy.ACCESSIBILITY_ID,
                "Create post"
            )
            self.click(post)
        
            # select_one = (
            #     AppiumBy.ACCESSIBILITY_ID,
            #     "Choose audience"
            # )
            # self.click(select_one)
            # time.sleep(1)

            # select_group = (
            #     AppiumBy.ACCESSIBILITY_ID,
            #     "Share with Figure 1 public"
            # )
            # self.click(select_group)

            add_title = (
                AppiumBy.ACCESSIBILITY_ID,
                "Case description"
            )
            self.click(add_title)
            self.type(add_title, "Post Title Testing")
            self.press_back()

            add_specialities = (
                AppiumBy.ACCESSIBILITY_ID,
                "Add specialty"
            )
            self.click(add_specialities)
            time.sleep(0.5)
            
            abdominal = (
                AppiumBy.ACCESSIBILITY_ID,
                "CASE_SPECIALTY_SEARCH_LIST_ITEM_0"
            )
            self.wait_for_presence(abdominal)
            self.click(abdominal)

            save = (
                AppiumBy.ACCESSIBILITY_ID,
                "Save"
            )
            self.click(save)

            save_as_draft = (
                AppiumBy.ACCESSIBILITY_ID,
                "Save as draft")
            self.swipe_until_visible(save_as_draft)
            self.click(save_as_draft)

            draft_popup = (AppiumBy.ACCESSIBILITY_ID, "Draft Saved")
            self.click(draft_popup)

            cross_button = (
                AppiumBy.ACCESSIBILITY_ID,
                "Go back"
            )
            self.click(cross_button)

            draft_popup = (AppiumBy.ACCESSIBILITY_ID, "Draft Saved")
            try:
                element = self.wait_for_presence(draft_popup)  
                element.click()
            except:
                logging.error("Draft not saved: popup did not appear.")
            logging.info("Post share executed successfully.")

        except Exception as e:
            logging.error(f"Error occurred in post_tab: {e}")
            raise


    def community(self):
        try:
            # ================== OPEN COMMUNITY TAB ==================
            community_tab = (
                AppiumBy.ACCESSIBILITY_ID,
                "Community"
            )
            self.click(community_tab)

            self.swipe_down()
            
            top_section = self.wait.until(
                lambda driver: driver.find_element(
                    AppiumBy.XPATH,
                    '//android.widget.HorizontalScrollView'))

            self.driver.execute_script("mobile: swipeGesture", {
                "elementId": top_section.id,
                "direction": "left",
                "percent": 0.9
            })
            logging.info("Swiped left Suggested profiles")

            # ================== MY COMMUNITIES SECTION ==================
            my_community_view = (AppiumBy.ACCESSIBILITY_ID,"My communities card_viewAll")
            self.click(my_community_view)

            open_group = (AppiumBy.ACCESSIBILITY_ID,"undefined_item_0")
            self.click(open_group)
            invite = (AppiumBy.ACCESSIBILITY_ID,"Invite")
            self.click(invite)
            time.sleep(0.5)
            self.go_back()
            about_group = (AppiumBy.ACCESSIBILITY_ID,"All about group")
            self.click(about_group)
            view_description = (AppiumBy.ACCESSIBILITY_ID, "View group description")
            self.click(view_description)
            time.sleep(0.5)
            self.go_back()
            about_group = (AppiumBy.ACCESSIBILITY_ID,"All about group")
            self.click(about_group)
            view_members = (AppiumBy.ACCESSIBILITY_ID, "View group members")
            self.click(view_members)
            time.sleep(0.5)
            self.go_back()
            my_groups = (AppiumBy.ACCESSIBILITY_ID, "Open my groups options")
            self.click(my_groups)
            create_group = (AppiumBy.ACCESSIBILITY_ID, "Create new group")
            self.click(create_group)
            time.sleep(0.5)
            self.go_back()
            time.sleep(1)
            self.go_back()
            time.sleep(1)
            self.go_back()
            time.sleep(1.5) 

            logging.info("My communities section executed successfully.")

            # ================== CASE LABS SECTION ==================
            case_labs = (AppiumBy.ACCESSIBILITY_ID,"case-lab-preview-card_viewAll")
            self.click(case_labs)

            first_lab = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "Community case lab card_item_0")
            if first_lab:
                first_lab[0].click()
                time.sleep(1)
                self.go_back()
                time.sleep(1)
                self.go_back()
            else:
                self.go_back()

            explore_lab = self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, "Community case lab card_exploreLab_1")
            if explore_lab:
                explore_lab[0].click()
                time.sleep(1)
                self.go_back()
            else:
                self.go_back()

            logging.info("Case labs section executed successfully.")

            # ================== PUBLIC GROUPS SECTION ==================
            public_group = (AppiumBy.ACCESSIBILITY_ID,"joinable-groups-preview-card_viewAll")
            self.swipe_until_visible(public_group) 
            self.click(public_group) 
            time.sleep(1)
            self.go_back()

            logging.info("Public groups section executed successfully.")

            # ================== EXPERT FEEDS SECTION ==================
            expert_feeds = (AppiumBy.ACCESSIBILITY_ID,"community-expert-feed-preview-card_viewAll")
            self.swipe_until_visible(expert_feeds)
            self.click(expert_feeds)
            time.sleep(1)
            self.go_back()

            logging.info("Expert feeds section executed successfully.")

            logging.info("Community tab executed successfully.")
            
        except Exception as e:
            logging.error(f"Error occurred in my_community: {e}")
            raise


    def search(self):
        try:
            # ================== OPEN SEARCH TAB ==================
            search_tab = (
                AppiumBy.ACCESSIBILITY_ID,
                "Search"
            )
            self.click(search_tab)

            self.type(search_tab, "PAnkk")
            self.driver.press_keycode(66)

            profiles_filter = (AppiumBy.ACCESSIBILITY_ID, "Search profiles")
            self.click(profiles_filter)

            clear = (AppiumBy.ACCESSIBILITY_ID, "Clear search")
            self.click(clear)
            self.driver.press_keycode(4)

            logging.info("Search tab executed successfully.")

        except Exception as e:
            logging.error(f"Error occurred in search: {e}")
            raise

    
    def my_feed(self):
        try:
            # ================== OPEN MY FEED TAB ==================
            feed_tab = (
                AppiumBy.ACCESSIBILITY_ID,
                "My Feed"
            )
            self.click(feed_tab)
            self.click(feed_tab)

            see_more = (AppiumBy.ACCESSIBILITY_ID, "See more")
            self.swipe_until_visible(see_more)
            self.click(see_more)
            
        except Exception as e:
            logging.error(f"Error occurred in my_feed: {e}")
            raise