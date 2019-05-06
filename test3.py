import pymysql
import random


dbinfo = {
    "user":"root",
    "password":"123456",
    "host":"127.0.0.1",
    "db":"lux"
}

def query(sql):
    '''
    查询数据库的方法，需要传入sql。
    '''
    db = pymysql.connect(**dbinfo)  # 连接数据库
    cur = db.cursor()  # 获取游标
    cur.execute(sql)  # 执行SQL
    res = cur.fetchall()  # 获取返回值
    db.close()
    return res

def commit(sql):
    '''
    修改数据库的方法，需要传入sql。
    '''
    db = pymysql.connect(**dbinfo)  # 连接数据库
    cur = db.cursor()  # 获取游标
    try:
        cur.execute(sql)  # 执行SQL
        db.commit()   # 应用更改
        return True
    except:
        return False



def reg(username,password,nickname,remark=""):
    qsql = "select * from bxgz where username = '{}';".format(username)
    res = query(qsql)
    if len(res) == 0:
        hid = random.randint(10000,9999999)
        sql = "insert into bxgz (id,username,password,nickname,remark) values ({id},'{username}','{password}','{nickname}','{remark}' );".format(id=hid,username=username,password=password,nickname=nickname,remark=remark)
        if commit(sql):
            print("恭喜你，注册成功！！！")
        else:
            print("对不起，系统异常！请稍后再试！")
    else:
        print("账号已存在，请重新输入")


def login(username,password):
    sql = "select * from bxgz where username = '{}';".format(username)
    res = query(sql)
    if len(res) == 0:
        print("账号不存在！！！")
        return False
    elif len(res) > 1:
        print("账号数据异常，请联系管理员！！！")
        return False
    else:
        if password == res[0][2]:
            print("登录成功，游戏愉快！")
            return True
        else:
            print("密码错误！！！")
            return False

        

print("--------------------")
print("|                   |")
print("|  白雪公主逃跑记   |")
print("|                   |")
print("--------------------")
print("尊敬玩家！欢迎来到白雪公主逃跑大世界的游戏中来。")
while True:
    xx = input("请选择【1.注册】或【2.登录】\n")
    if xx == "1":
        username = input("请输入账号：")
        password = input("请输入密码：")
        nickname = input("请输入昵称：")
        reg(username,password,nickname,remark="")
    elif xx == "2":
        username = input("请输入账号：")
        password = input("请输入密码：")
        while login(username,password):
            print("你是白雪公主，遭到王后的迫害，正在逃亡中。。。")
            bxinfo = {
                "life":50,
                "ko":10
            }
            print("你的生命值是50，攻击力是10.")
            xx = input("你刚刚逃出城堡，面前有两条录，一条是去【1.森林】，一条去【2.河边】，你要怎么走？\n")
            if xx == "1":
                xx = input("你顺利逃进了森林，不小心遇到了往后派来的士兵，选择【1.逃跑】还是【2.战斗】？\n")
                if xx == "1":
                    print("啊，转身就遇到了更多的士兵，是的，你被捕啦！！")
                elif xx == "2":
                    sbinfo = {
                        "life":20,
                        "ko":6
                    }
                    while sbinfo["life"] > 0:
                        # 这里有一个BUG，有可能被会出现白雪公主被反杀，所以得考虑这种情况。
                        bx = random.randint(0,10)
                        sb = random.randint(0,6)
                        if bx >= sb:
                            sbinfo["life"] = sbinfo["life"] - (bx-sb)
                            print("白雪公主打了士兵一棒棒！！！")
                        else:
                            bxinfo["life"] = bxinfo["life"] - (sb-bx)
                            print("士兵打了白雪公主一耳光！！！")
                    print("经过几个回合的你来我往，白雪公主战胜了士兵！！！")
                    print("此时，你的生命值是【{}】,攻击力是【{}】".format(bxinfo["life"],bxinfo["ko"]))
                    print("白雪公主，继续逃跑。。。")
                    print("逃跑中。。。")
                    while True:
                        xx = input("经过3天的逃亡，白雪公主，饿的不行了。突然出现了一个女巫，在路边卖【十全大补丸】，但是她的十全大补丸有问题，有50%的几率会导致\
                            掉血50%，或者增加10点攻击，不过都会让白雪公主吃饱。你选择是【1.吃】还是【2.不吃】？\n")
                        if xx == "1":
                            x = random.choice("01")
                            if x == "0":
                                bxinfo["life"] = int(bxinfo["life"]/2)
                                print("掉血")
                                print("此时，你的生命值是【{}】,攻击力是【{}】".format(bxinfo["life"],bxinfo["ko"]))
                            else:
                                bxinfo["ko"] = bxinfo["ko"] + 10
                                print("增加攻击")
                                print("此时，你的生命值是【{}】,攻击力是【{}】".format(bxinfo["life"],bxinfo["ko"]))
                            break
                        elif xx == "2":
                            print("对不起，你饿死了！")
                            break
                        else:
                            print("请选择正确的选项")
            elif xx == "2":
                print("你不会游泳，淹死了！")
            else:
                print("请选择正确的选项")
    else:
        print("选择无效，请输入正确的选项！！！")