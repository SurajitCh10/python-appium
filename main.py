import time
from appium import webdriver



desired_caps = {
            "platformName": "android",
            "appActivity": "com.atg.world.activity.SplashActivity",
            "appWaitDuration": 50,
            "uiautomator2ServerLaunchTimeout": 50000,
            "uiautomator2ServerInstallTimeout": 50000,
            "appPackage": "com.ATG.World",
            "deviceName": "emulator-5554",
            "driver": "http://localhost:4723/wd/hub"}

driver.find_element_by_id("permission_id").click()
time.sleep(2)

driver.find_element_by_id("getStarted").click()
time.sleep(2)

driver.find_element_by_id("login").click()
time.sleep(2)

driver.find_element_by_id("permission_id").click()
time.sleep(2)

driver.find_element_by_id("email_id").send_keys("wiz_saurabh@rediffmail.com")
time.sleep(2)

driver.find_element_by_id("password_id").send_keys("Pass@123")
time.sleep(2)

