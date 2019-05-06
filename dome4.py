import pymysql

dbinfo={
    "user":"root",
    "password":"123456",
    "host":"127.0.0.1",
    "db":"student"
}
def select(sql):
    db=pymysql.connect(**dbinfo)
    cur=db.cursor()
    cur.execute(sql)
    res=cur.fetchall()
    return res

sql1="select * from st where name='aa' ;"
print(select(sql1))

def de(sql):
    db=pymysql.connect(**dbinfo)
    cur=db.cursor()
    cur.execute(sql)
    db.commit()
    print("删除成功")

sql="delete from st where id=3;"
de(sql)