'''
 selenium 的键盘和鼠标事件
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

# def keyboard():
"""
    键盘事件：
        常用的键值
        - Keys.BACK_SPACE：删除键
        - Keys.SPACE：空格键
        - Keys.TAB：Tab键
        - Keys.ESCAPE：回退键
        - Keys.ENTER：回车键
        - Keys.CONTROL,”a”：组合键，Ctrl + A
        - Keys.CONTROL,”x”：组合键，Ctrl + X
        - Keys.CONTROL,”v”：组合键，Ctrl + V
        - Keys.CONTROL,”c”：组合键，Ctrl + C
        - Keys.F1：F1键
        - Keys.F12：F12键
    """

#     driver = webdriver.Chrome(executable_path="./dirver\chromedriver.exe")
#     driver.get('http://www.baidu.com')

#     driver.find_element_by_id("kw").send_keys("pythons")
#     time.sleep(3)

#     # driver.find_element_by_id("kw").send_keys(keys.B)
#     driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

#     time.sleep(3)

#     driver.find_element_by_id("kw").send_keys(Keys.ENTER)

#     time.sleep(3)
#     driver.quit()

# keyboard()

'''
鼠标事件
   """
        鼠标事件:
        - perform()：执行所有ActionChains存储的行为
        - context_click()：右击
        - double_click()：双击
        - drag_and_drop()：拖动
        - move_to_element()：悬停
    """
'''
def mouse():
   

    driver = webdriver.Chrome(executable_path="./dirver\chromedriver.exe")
    driver.get('http://www.baidu.com')

    # driver.find_element_by_id("kw").send_keys("pythons")
    # driver.find_element_by_id("su").click()
    #鼠标移动
    # sz = driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
    # ActionChains(driver).move_to_element(sz).perform()

    # 右键

    # news = driver.find_element_by_link_text("新闻")
    # ActionChains(driver).context_click(news).perform()
    

    # 双击
    news = driver.find_element_by_link_text("新闻")
    ActionChains(driver).double_click(news).perform()


    time.sleep(5)
    driver.quit()

# mouse()   

def iframe():
    driver = webdriver.Chrome(executable_path="./dirver\chromedriver.exe")
    driver.get('https://passport2.eastmoney.com/pub/login')


    driver.maximize_window()

    iframe = driver.find_element_by_id("frame_login")
    # 到iframe作用域
    driver.switch_to_frame(iframe)   

    driver.find_element_by_id("txt_account").send_keys("111111111")

    time.sleep(3)

    driver.switch_to_default_content()
    ele = driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div')
    print(ele.text)

iframe()