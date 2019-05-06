'''
1、注册/登录
2、白雪公主逃跑记

'''
import random
print("--------------------")
print("|                   |")
print("|  白雪公主逃跑记   |")
print("|                   |")
print("--------------------")
print("尊敬玩家！欢迎来到白雪公主逃跑大世界的游戏中来。")
userinfo = {"username":"admin","password":"1"}

def checkuser(username):
    '''
    检查账号是否已经存在
    '''
    for i in userinfo:
        if username == userinfo.get(i):
            return False
    return True

def login():
    '''
    登录功能
    '''
    username = input("请输入账号：")
    password = input("请输入密码：")
    if username == userinfo["username"] and password == userinfo["password"]:
        return True
    else:
        print("账号或密码不对，请检查后输入！") 
        return False

xuanliang = input("请选择【1.登录】或【2.注册】:")
if xuanliang == "1":
    if login():
        print("你是白雪公主，遭到王后的迫害，正在逃亡中。。。")
        xx = input("你刚刚逃出城堡，面前有两条录，一条是去【1.森林】，一条去【2.河边】，你要怎么走？")
        if xx == "1":
            xx = input("你顺利逃进了森林，不小心遇到了往后派来的士兵，选择【1.逃跑】还是【2.战斗】？")
            if xx == "1":
                print("啊，转身就遇到了更多的士兵，是的，你被捕啦！！")
            elif xx == "2":
                bx = random.randint(0,10)
                sb = random.randint(0,10)
                print(bx, sb)
                if bx+5 >= sb:
                    print("白雪公主真棒！")
                else:
                    print("白雪公主输了，被捕了！")
        elif xx == "2":
            print("你不会游泳，淹死了！")
        else:
            print("请选择正确的。。。")
elif xuanliang == "2":
    username = input("请新建账号：")
    if checkuser(username):
        password1 = input("请输入密码：")
        password2 = input("请确认密码：")
        if password1 == password2:
            userinfo["username"] = username
            userinfo["password"] = password2
            if login():
                pass

        else:
            print("注册失败，前后密码不一致！")
    else:
        print("账号已存在，请重新输入！")
else:
    print("请选择正确的选项！！")