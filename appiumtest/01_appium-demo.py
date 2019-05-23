from appium import webdriver
import time


def get_driver():
    """
        获取设备driver
    """
    desired_caps = {}
    desired_caps['platformName'] = 'Android'                      #打开什么平台的app
    desired_caps['platformVersion'] = '5.1.1'                     #安卓的版本
    desired_caps['deviceName'] = 'oppo a33m'                        #型号
    desired_caps['appPackage'] = 'io.appium.android.apis'          #安卓的每一个软件的唯一标识，获取软件package和activity
                                                                    # 的命令：adb shell dumpsys activity | findstr "mFocusedActivity"
    desired_caps['appActivity'] = '.ApiDemos'                       #流云 activity：软件的启动页面的名字，软件页面唯一的id
    desired_caps['unicodeKeyboard']=True                            #设置键盘支持中文
    desired_caps['resetKeyboard']=True                               #设置appium的默认键盘
# 去打开软件，并且返回当前软件的driver对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    return driver

driver=get_driver()
# driver.find_element_by_accessibility_id("App").click()
ele = driver.find_element_by_android_uiautomator('new UiSelector().text("App")').get_attribute("name")
print(ele)


# driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Search"]').click()          #横屏会找不到
# driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Invoke Search"]').click()   

# driver.find_element_by_id("android:id/text1").click()             #在多个id相同时会直接点击第一个
# driver.find_element_by_accessibility_id("Search").click()          #有问题，横屏找不到
# driver.find_element_by_accessibility_id("Invoke Search").click()

# driver.find_element_by_id("io.appium.android.apis:id/txt_query_appdata").send_keys("hello appium")

# driver.find_element_by_xpath(
#     "//android.widget.EditText[@resource-id='io.appium.android.apis:id/txt_query_appdata']"
#     ).send_keys("hello appium")

time.sleep(5)
driver.quit()


# id


# accessibility_id


# xpath


# new Uiselector().text('发送')