hhh=123
if type(hhh) is int:
    print("kfhsijdhf")
elif hhh<3:
    print("vfvvvvv")
else:
    print("fkshd")

shuzu = ["gsdhfghkj","fffff","12321","fjjf8"]
#判断循环要用：
for i in shuzu:
    print(i)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print("hell,"+i)

print("------------------")
zidian={
    "key":"velue",
    "姓名":"hjhlkjh",
    "性别":"男"
}
for i in zidian:
    print(zidian.get(i))

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)


import itchat

itchat.auto_login(hotReload=True)

itchat.send()
allfriends=itchat.get_friends()
for i in allfriends:
    print(i)



