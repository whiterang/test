# 流云 2019/4/24 22:40:26
# 作业：
# 1. 定义一个叫 Cat的类，属性有：年龄5岁；名字叫：tomcat；它能抓老鼠
# 2. 用初始化类的方式去修改这个猫的类名字：菲菲



class Cat():
    age=5
    name="tom"
    def cat(self):
        print("它能抓老鼠")
    def __init__(self,name):
  
        self.name=name

if __name__ == "__main__":
    a = Cat("ff")
    print(a.name)
