"""
    Appium的二次封装
"""
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class PyAppium():

    def __init__(self, url="http://localhost:4723/wd/hub", desired_caps={}, timeout=10):
        """
            构造方法
        """
        self._driver = webdriver.Remote(url, desired_caps)
        self._timeout = timeout

    def get_origina_driver(self):
        """
            获取appium原始的driver
        """
        return self._driver

    def find_element(self, locator):
        """
            查找单个元素
            参数：
                id: "id"
                xpath: "xpath"
                accessibility_id: "accessibility id"
                android_uiautomator: "-android uiautomator"
        """
        if not isinstance(locator, tuple):
            raise Exception("输入的参数必须是(by, value)格式!")

        try:
            return WebDriverWait(self._driver, self._timeout).until(lambda s: s.find_element(*locator))
        except:
            print("未找到元素{}!".format(locator))
            return []

    def find_elements(self, locator):
        """
            查找多个元素
            参数：
                id: "id"
                xpath: "xpath"
                accessibility_id: "accessibility id"
                android_uiautomator: "-android uiautomator"
        """
        if not isinstance(locator, tuple):
            raise Exception("输入的参数必须是(by, value)格式!")

        try:
            return WebDriverWait(self._driver, self._timeout).until(lambda s: s.find_elements(*locator))
        except:
            print("未找到元素{}!".format(locator))
            return []

    def type_zh(self, locator, keywords):
        """
            支持中文的输入
        """
        e = self.find_element(locator)
        if isinstance(e, list):
            raise Exception("未找到locator，请检查传递的参数")

        e.send_keys(keywords)

    def type(self, locator, keywords):
        """
            快速的输入，不支持中文
        """
        e = self.find_element(locator)
        if isinstance(e, list):
            raise Exception("未找到locator，请检查传递的参数")

        self._driver.set_value(e, keywords)

    def click(self, locator):
        """
            点击操作
        """
        e = self.find_element(locator)
        if isinstance(e, list):
            raise Exception("未找到locator，请检查传递的参数")

        e.click()

    def does_exist(self, locator):
        """
            动态判断元素是否存在：容错率非常高
        """
        e = self.find_element(locator)
        if isinstance(e, list):
            return False    # 元素不存在
        else:
            return True     # 元素存在


if __name__ == "__main__":
    
    pyappium = PyAppium(desired_caps=Config.desired_caps)

    # locator = ("id", "android:id/text1") 
    # locator = ("xpath", '//android.widget.TextView[@content-desc="Accessibility"]')
    # locator = ("accessibility id", "Accessibility")
    # locator = ("-android uiautomator", 'new UiSelector().text("Accessibility")')
    # pyappium.find_element(locator).click()

    app = ("accessibility id", "App")
    app_search = ("accessibility id", "Search")
    app_search_invoke = ("accessibility id", "Invoke Search")
    app_search_invoke_appdata = ("id", "io.appium.android.apis:id/txt_query_appdata")

    # pyappium.click(app)
    # pyappium.click(app_search)
    # pyappium.click(app_search_invoke)
    # pyappium.type(app_search_invoke_appdata, "hello appium!")
    # pyappium.type_zh(app_search_invoke_appdata, "hello appium!")

    print(pyappium.does_exist(app))
