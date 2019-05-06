# 今天是2019年的4月23日，
# 请通过编程的手段来确认今天是今年的第几天。
# '''
# 有这么一段字符串
# 【k32j5g3k4j65b345lk6h435lk6jnn234lkjn32l4k5hn3k4lj534k6】，
# 卿通过编程的手段来确认，第一次出现
#  【字母数字字母】这种排序的位置
#  ，是第几位
# '''

year=2019
month=4
day=23
sum=0
i=0
if year%400==0 or (year%4==0 and year%100!=0):
    mon=[31,29,31,30,31,30,31,31,30,31,30,31]
else:
    mon=[31,28,31,30,31,30,31,31,30,31,30,31]
for  i in range(month-1):
    sum = sum + mon[i]
print("今天是2019年的4月23日，今天是今年的第"+str(sum+day)+"天")



s='k32j5g3k4j65b345lk6h435lk6jnn234lkjn32l4k5hn3k4lj534k6'
l=list(s)
n = len(l)
i=0
while i+2<n:
    if l[i].isalpha()==True and l[i+1].isdigit()==True and l[i+2].isalpha()==True:
        print(i);
        break
    i = i + 1
