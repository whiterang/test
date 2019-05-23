import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

class TestCaseLogin(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome(executable_path="./driver/chromedriver.exe")
        
        self.driver.get('http://localhost:8080/morning')
    


    def tearDown(self):
        self.driver.quit()
    
    def test_login_success(self):
        self.driver.find_element_by_link_text("登录").click()
        # time.sleep(5)
        self.driver.find_element_by_id("adminNo").send_keys("1141893331@qq.com")
        self.driver.find_element_by_id("password").send_keys("a123456")
        # self.driver.find_element_by_id("btn_login").click()
        WebDriverWait(self.driver,10).until(lambda s: s.find_element("id",'btn_login')).click()
        time.sleep(5)
        ele = self.driver.find_element_by_xpath('//*[@id="header-content-nav"]/ul/li[1]/a')
        self.assertEqual(ele.text, "配件")


  
        print("这是登录成功的测试用例")
        
    def test_login_failed(self):
        self.driver.find_element_by_link_text("登录").click()
        # time.sleep(5)
        self.driver.find_element_by_id("adminNo").send_keys("1141893331@qq.com")
        self.driver.find_element_by_id("password").send_keys("a1234567")
        self.driver.find_element_by_id("btn_login").click()

        ele = self.driver.find_element_by_xpath('//*[@id="verifyCheck"]/div/div[1]/label')
        # self.assertEqual(ele.text, "你输入的密码和账户名不匹配，请确认后重新输入。")
        self.assertNotEqual(ele.text, "")

        print("这是登录失败的测试用")