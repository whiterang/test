# def add(a=1, b=1):
#     return a + b
# c = add(b=2)
# print(c)


def get_value(dic, key):
    return dic.get(key)

if __name__ == "__main__":
    
    userinfo={"username":"hjhj","password":"123243"}
    username= get_value(userinfo, "username")
    print(username)



    # a = 1
# b = 1
# c = a + b
# print(c)


# python中以def开头
# 方法名：只能以下划线或者小写字母开头；方法名可以包括英文数字特殊的符号_，以
# ()：参数，调用方法的时候，可以传一些值给这个方法：数字，字母，list[],字典{}，类对象
# :结尾
# 隔行：代码tab隔空
# return: 方法执行完之后，需要返回一个值给调用的入口；代码复用
# 方法的调用：add(a, b)
# 变量接收方法的返回值
def add(a, b):
    """
        加法的封装方法
    """
    c = a + b
    return c

def add1(a=1, b=1):
    """
        有默认的方法
    """
    return a + b

def get_value(dic, key):
    """
        获取一个字典的值
    """
    return dic.get(key) # = "ljtest"


def str_format():
    """
        拼接字符串
    """
    lang = "python"

    # format格式
    strs = "{}好难学呀！".format(lang)
    print(strs)

    # %s
    lang = "java"
    strs1 = "%s更难学呀！" %lang
    print(strs1)




# 告诉python，只有在当前py模块中运行的时候，才运行下面包含的代码
if __name__ == "__main__":

    str_format()
    # 传其他类型的参数
    # userinfo = {"username":"ljtest", "password":"123456"}
    # username = get_value(userinfo, "username") #= "ljtest"
    # print(username)

    #  1.方法没有默认值
    # c = add(1, 2)
    # print(c)

    # 2. 方法默认值
    # add()
    # 如果没有传参数，a=1 b=1
    # c = add1()
    # print(c)
    # c = add1(2, 3)
    # print(c)

    # 3. 传递一部分参数
    # c = add1(b=2, a=1)
    # print(c) 


    # 类和对象
# 动物-抽象的概念，所有实体动物的集合（猫、狗、羊、猴子。。。）
# 对象-具体对应的动物了，猫、狗、羊


# 人-抽象的类，模板，吃喝xx赌，眼睛、鼻子
# 对象-代妃、郭丰志。。。



"""
    1. 类定义：以class开头，
    2. 类名：以大写的字母开头
"""
class Test():
    username = "代妃"
    age = 18
    # 构造方法：初始化方法
    def __init__(self, user_name, _age):
        self.username = user_name   # 调用
        self.age = _age

    def __age(self):
        return 18

    def get_age(self):
        print(self.__age())

# 类传递传数
a = Test("苏格", 17)
print(a.username)
print(a.age)
a.get_age()


class People():

    # 成员变量：类的变量，类的属性
    username = "代妃"
    sex = "女"
    age = 18

    # 成员方法：类的方法
    # 以self作为首个参数，固定的写法
    # def是在定义一个方法，如果不写在类里面，就是一个普通方法；但是写在类里面，成员方法
    def eat(self):
        print("人可以吃东西！")

    def run(self):
        print("人可以跑！")


# 实例化一个类对象，实例化对象
# df：变量，实例化对象
# 整个过程就叫实例化对象/初始化对象
b = People()


# print("我的名字叫:{}".format(b.username))   # 调用成员变量
# b.eat()                                    # 调用成员方法