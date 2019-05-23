from selenium import webdriver
# import time
# def main():
#     b=webdriver.Chrome()
#     b.get('http://www.baidu.com')
#     time.sleep(5)
#     b.quit()
# if __name__ == '__main__':
#     main()


driver=webdriver.Chrome(executable_path="./dirver\chromedriver.exe")
driver.get('http://www.baidu.com')
# ele = driver.find_element_by_id("kw")


ele = driver.find_element_by_xpath('//*[@id="kw"]')
ele.send_keys("chromedriver")
ele=driver.find_element_by_id("su")

ele.click()
# driver.quit()

"""
    selenium的八大元素定位
"""


from selenium import webdriver

driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe")
driver.get("https://www.baidu.com")

# 1. id值定位：定位最准备
# ele = driver.find_element_by_id("kw")
# ele.send_keys("ljtest")

# 2. name值定位
# ele = driver.find_element_by_name("wd")
# ele.send_keys("ljtest")

# 3. class值定位
# ele = driver.find_element_by_class_name("s_ipt")
# ele.send_keys("ljtest")

# 4. xpath路径定位：用得非常之多
# ele = driver.find_element_by_xpath("//*[@id='kw']")
# ele.send_keys("ljtest")

# 5. css selector
# driver.find_element_by_css_selector('#kw').send_keys("ljtest")

# 6. link_text:链接的文字
# driver.find_element_by_link_text("新闻").click()

# 7. partial_link_text:链接的一部分文字
# driver.find_element_by_partial_link_text("hao").click()

# 8. tag_name:用得很少，一般都不怎么用
# e = driver.find_element_by_tag_name('form')
# print(e)


#能用id就用id，不能用id就用xpath

# 运行结束后，关闭浏览器
# driver.quit()