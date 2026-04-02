This project contains Appium automation scripts using Python.

To install requirements, run:
pip install -r requirements.txt
appium driver install uiautomator2

To run all tests, start the Appium server, connect your device or emulator, and run:
pytest -v --html=report.html --self-contained-html

To run a specific test, use:
pytest -m profile_smoke --html=report.html --self-contained-html 



-----For testing with a new APK file-------

Add the APK file inside the apks/ folder.

Update the APK path in core/base.py:
Change the APK name in the following line as per the new file:
apk_path = os.path.join(base_dir, "..", "apks", "app-release-missingid.apk")


-------Configuration changes required for smoke tests--------------
Like - pytest -m profile_smoke --html=report.html --self-contained-html

In core/base.py:
Uncomment the following line to keep the app state between tests:
"noReset": True,               

In conftest.py:
Comment the below line to avoid reinstalling the app before driver start:
#install_app_once()           


--------Automated Test Coverage – High-Level Steps-------------

Launch the application and navigate through Home → Menu → Figure 1 app

Detect user authentication state

If logged out → perform Sign In

If logged in → Log out and re-login to validate the full flow

Validate successful login and session stability

Profile Module Automation-------

Navigate to Profile section

Update Profile Picture using Camera and Gallery

Validate Followers & Following navigation and follow/unfollow actions

Edit profile details (Profession, Specialty, About) and verify updates

Send invitations via Invite to My Network

Manage Interests (search, select, and add)

Update About section (Experience, Education, Affiliations)

Drawer Module Automation------

Navigate to Drawer Menu

Delete posts from Saved section

Delete posts from Drafts section

Validate My Network profiles and search functionality

Navigate all tabs in Help & Feedback

Verify Account Settings and related sub-features

Validate Invite Colleagues flow and system share options