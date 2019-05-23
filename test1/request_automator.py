from utils.utils_db import query 
from utils.utils_request import request
from utils.utils_excel import read_excel 

# 1. 取出测试用例
sheet_name = "Sheet1"
excel_path = "testcases\注册用例模板.xlsx"
testcases = read_excel(excel_path, sheet_name)

for testcase in testcases:
    print("-------------------------")
    url = testcase[1]                  
    method = testcase[5]              
    playload = eval(testcase[7])        
    http_expect_code = int(testcase[8])     
    response_expect_code = int(testcase[9])

    response = request(url=url, method=method, json=playload)
    try:
        # print(response.json().get("code"))
        # print(response.status_code)
        # print(http_expect_code)
        # print(type(response_expect_code))
        assert response.status_code == http_expect_code             
        assert response.json().get("code") == response_expect_code 

        
        username = playload.get("username")
        password = playload.get("password")
        dbinfo = {"user":"root","password":"123456","host":"118.24.29.59","db":"lux"}
        sql = "select * from tbl_user where username='{}' and password='{}'".format(username, password)
        res = query(sql, dbinfo)
        # print(res)
        assert len(res) == 1
  
        print("测试用例执行成功！")
        print("-------------------------")
    except:
        print(response.text)
        print("测试用例执行失败了！")
        print("-------------------------")