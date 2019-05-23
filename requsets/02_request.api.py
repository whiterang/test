import requests

import pymysql

def get_dome():
    url = "http://118.24.29.59:5000/"

    res=requests.get(url)
    print(res.text)



def post_from_data():
    pass
    

def post_json_data():

    url = "http://118.24.29.59:5000/userLogin/"
    playload = {"username":"test", "password":"test", "captcha":"123456"}

    response = requests.post(url=url,json=playload)
    print(response.text)


def requests_step_demo():

# 1.构造请求
    url = "http://118.24.29.59:5000/userLogin/"
    playload = {"username":"test", "password":"test", "captcha":"123456"}

    response = requests.post(url = url,json = playload)
# 2.断言http响应状态码
    http_code = response.status_code
    assert http_code == 200
# 3.判断接口响应数据

    data = response.json()
    code =data.get("code")
    assert code == 200

# 4.查询数据库，验证数据库数据是否正确


dbinfo={
    "user":"root",
    "password":"123456",
    "host":"118.24.29.59",
    "db":"lux"
}



def select(sql,dbinfo):
    db=pymysql.connect(**dbinfo)
    cur=db.cursor()
    cur.execute(sql)
    res=cur.fetchall()
    return res


sql = "select * from tbl_user where username='test' and password='test';"
result = select(sql=sql,dbinfo=dbinfo)
assert len(result) == 1
# get_dome()
# post_json_data()

print("登录接口的测试用例成功")