
# a=0
# H=0
# while True:
#     num = input("请输入一个数字")
#     num1 = int(num)
#     a += 1
#     if a == 1:
#         max=num1
#     else:
#         if num1>max:
#             max=num1
#     if a < 10:
#         H = int(num1)+int(H)
#     elif a >= 10:
#         H = int(num1) + int(H)
#         print("合为",int(H))
#         print("最大值",max)
#         print("平均值",int(H)/10)
#         break



# a=int(input("请输入第一个边"))
# b=int(input("请输入第二个边"))
# c=int(input("请输入第三个边"))
# if a==b==c:
#      print("等边三角形")
# elif a==b or a==c or b==c:
#      print("等腰三角形")
# elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
#     print("直角三角形")
# elif a+b>c or a+c>b or b+c>a:
#      print("普通三角形")
# else:
#     print("不构成三角形")



# A=input("第一个数")
# B=input("第二个数")
# A=int(A)+int(B)
# B=int(A)-int(B)
# A=int(A)-int(B)
# print("A",A,"B",B)

#
# root=1
# admin=12345
# a=0
# while True:
#     if a<int(3):
#         A = int(input("请输入密码"))
#         if admin==A:
#             print("密码正确")
#         elif a==2:
#             print("密码错误三次，系统已锁定")
#             a += 1
#         else:
#             a += 1
#             print("密码错误，请重新输入")
#     else:
#         break

#
# for i in range(8):
#     for j in range(0, 8- i):
#         print(end=" ")
#     for k in range(8 - i, 8):
#         print("*", end=" ")
#     print("")

#while 乘法表
# i=1
# while i<10:
#     j=1
#     while j<=i:
#         print('%d*%d=%d\t'%(j,i,i*j),end=(''))
#         j+=1
#     print('')
#     i+=1
# print('')

# for y in range(-9,0):
#     for x in range(1,-y+1):
#         print("%d x %d = %d"%(x,-y,x*(-y)),end=" ")
#         print(end="")
#     print("")


# h=20
# D=0
# l=0
# while True:
#      if l>=20 or int(l)+3>=20:
#          print(D)
#          break
#      elif l<20:
#          D += 1
#          l += 1

# import  random
# num1=random.randint(0,190)
# i = 0
# n=100
# gold=2000
# print("游戏开始\n请猜0-190之间的数字，答对有奖励哦")
# while True:
#     if n>=1:
#        i += 1
#        print("第",i,"次")
#        num = input("请输入你要猜的数字")
#        gold -= 500
#        print("当前金币数",gold)
#        if num1 == int(num):
#             print("猜对了！")
#             print("本次幸运数字为：", int(num1), "，本次猜了", i, "次", )
#             print("\n获得万元大礼包")
#             n =n - 100000
#             break
#        elif num1 < int(num):
#             print("猜的大了")
#        elif num1 > int(num):
#             print("猜的小了")
#
#        if gold <= 0:
#             t = int(input("是否继续挑战  \n输入任意数游戏继续\n输入0   游戏结束"))
#             if t >= 1:
#                 print("=================极力抢救===============")
#             else:
#                 print("不会吧不会吧不会有人怂了吧\n不太行啊小老弟")
#                 n = n - 100000
#                 break
#     elif n <= 0:
#         print("游戏结束")
#         break


# # Python程序来查找用户提供的数字的阶乘。
# num = int(input("输入数字: "))
# factorial = 1
# # 检查数字是负数，正数还是零
# if num < 0:
#  print("抱歉，负数不存在阶乘")
# elif num == 0:
#    print("0的阶乘是1")
# else:
#     for i in range(1,num + 1):
#         factorial = factorial*i
# print(num,"的阶乘是",factorial)