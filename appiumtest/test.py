from appium import webdriver

def get_driver():
    """
        获取设备driver
    """
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.2' // 改我
    desired_caps['deviceName'] = 'Redmi4X'  // 改我
    desired_caps['appPackage'] = 'io.appium.android.apis'
    desired_caps['appActivity'] = '.ApiDemos'
    desired_caps['unicodeKeyboard']=True
    desired_caps['resetKeyboard']=True

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    return driver
    
def test():
    """
        查找单个元素
    """
    # 获取driver
    driver = get_driver()

    #  通过id获取元素:最准确
    app = driver.find_element_by_id("android:id/text1")
    app.click()

    # 返回键
    driver.back()

    # 通过text获取元素
    Animation = driver.find_element_by_android_uiautomator('new UiSelector().text("Animation")')
    Animation.click()

    # 返回键
    driver.back()

    # 通过content-desc来获取元素
    app = driver.find_element_by_accessibility_id("App")
    app.click()

    # 返回键
    driver.back()

    # 通过xpath获取:使用最多
    media = driver.find_element_by_xpath("//android.widget.TextView[@text='Media' and @content-desc='Media']")
    media.click()


if __name__ == "__main__":
    test()
