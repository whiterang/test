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
'''
键盘事件
1.输入字符串
2.按键
3.返回
'''
def keyboard_event():
    driver = get_driver()
    driver.find_element_by_accessibility_id("App").click()
    driver.find_element_by_accessibility_id("Search").click() 
    driver.find_element_by_accessibility_id("Invoke Search").click() 
    #支持中文，非常慢
    driver.find_element_by_id("io.appium.android.apis:id/txt_query_appdata").send_keys("hello appium")
    #set_value 不支持中文，快速
    e = driver.find_element_by_id("io.appium.android.apis:id/txt_query_appdata")
    driver.set_value(e,"hello appium!")

    #返回
    driver.back()

    # 按键
    # driver.press_keycode()
'''
鼠标事件
    1.点击
    2.滑动
'''
def mouse_event():
    driver = get_driver()
    driver.press_keycode(3)
    import time
    time.sleep(3)

# 以左上角为原点
    driver.swipe(0,800,800,800)

if __name__ == "__main__":
    pass