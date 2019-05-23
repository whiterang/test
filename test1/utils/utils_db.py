import pymysql

def query(sql,dbinfo):
    '''
    查询数据库的方法，需要传入sql。
    '''
    db = pymysql.connect(**dbinfo)  # 连接数据库
    cur = db.cursor()  # 获取游标
    cur.execute(sql)  # 执行SQL
    res = cur.fetchall()  # 获取返回值
    return res    

if __name__ == "__main__":
        dbinfo = {"user":"root","password":"123456","host":"118.24.29.59","db":"lux"}
        sql = "select * from tbl_user where username='{}' and password='{}'".format("user3322", "123")
        res = query(sql, dbinfo)
        print(res)