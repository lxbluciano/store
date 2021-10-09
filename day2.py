import random

num1=random.randint(10,90)
i = 0
city = 3
while True:
   num = input("请输入一个数字")
   if num1 == int(num):
        print("猜对了")
        break
   elif num1 < int(num):
        print("猜的大了")
   elif num1 > int(num):
        print("猜的小了")
       # break
   i += 1
   if i >= city:
        print(int(num1))
        break