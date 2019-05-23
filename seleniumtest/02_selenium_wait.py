from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome(executable_path="./dirver\chromedriver.exe")

driver.get('http://www.baidu.com')

driver.find_element_by_id("kw").send_keys("hello world!")

ele=WebDriverWait(driver,10).until(lambda s: s.find_element("xpath",'//*[@id="container"]/div[2]/div/div[2]/span'))
print(ele.text)

driver.quit()