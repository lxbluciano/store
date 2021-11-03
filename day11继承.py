# import time
# class OldPhone:
#     __pinpai = ""
#
#     def setpinpai(self,pinpai):
#         if pinpai=="":
#             print("你搁这儿跟谁呢")
#         else:
#             self.__pinpai=pinpai
#
#     def getpinpai(self):
#         return self.__pinpai
#
#     def dadh(self,c):
#
#         print("正在给",c,"打电话")
#
#     def showMe(self):
#         print("这个手机的牌子是",self.__pinpai)
#
# class newphone(OldPhone):
#     def call(self,c):
#         super().dadh(c)
#
#         print("语音拨通中")
#         for i in range(8):
#             print(".", end="")
#             time.sleep(1)
#
#     def jeishao(self):
#         print("品牌为",super().getpinpai(),"的手机很好用")
#
# Phone=newphone()
#
# c=input("请输入名字")
# Phone.setpinpai("锤子")
# Phone.jeishao()
# Phone.showMe()
# Phone.call(c)

"""
要求：
1、定义厨师类，有姓名和年龄的属性，且属性私有化，提供相应的getXxx与setXxx方法，提供无返回值的无参数的蒸饭方法；
2、定义厨师的子类，该类中要求只能写一个无返回值的无参数的炒菜的方法，其他的方法不能写；
3、定义厨师的子类的子类，重写所有父类的方法，每个方法的内容只需打印一句话描述方法的功能即可；(蒸饭，炒菜)
4、定义测试类，创建厨师的子类的子类（厨师的孙子类）对象，使用该对象，对厨师类中的姓名和年龄属性赋值，并获取赋值后的属性值打印到控制台上；
5、使用厨师的孙子类对象调用该对象除了getXxx与setXxx以外的其他方法；
"""


class cooking:
    __username = ""
    __age = 0

    def set_username(self, username):
        if username == "":
            print("你没名字？")
        else:
            self.__username = username

    def get_username(self):
        return self.__username

    def set_age(self, age):
        if 130 >= age >= 0:
            self.__age = age
        else:
            print("你是没出生还是打破了世界纪录？")

    def get_age(self):
        return self.__age

    def cook(self):
        return "蒸饭的方法:..."


class fry_cook(cooking):

    def fry(self):
        return "炒菜的方法：..."


class cook_dinner(fry_cook):

    def cook(self):
        print("大厨%s正在通过%s做饭" % (super().get_username(), super().cook()))

    def fry(self):
        print("大厨%s正在通过%s炒菜" % (super().get_username(), super().fry()))

    def age(self):
        print("大厨%s今年已经%d岁了" % (super().get_username(), super().get_age()))


cook = cook_dinner()
cook.set_username("张三")
cook.set_age(20)
print(cook.get_username(), cook.get_age())
cook.cook()
cook.fry()
cook.age()


# i.	人：年龄，性别，姓名。
#
# ii.	现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。
#
# iii.	现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。

class person:
    __age = 0
    __sex = ""
    __username = ""

    def set_age(self, age):
        if age > 120 or age < 0:
            print("你是没出生还是打破了世界纪录？")
        else:
            self.__age = age

    def get_age(self):
        return self.__age

    def set_sex(self, sex):
        if sex == "男" or sex == '女':
            self.__sex = sex
        else:
            print("你就是传说中的秀吉吗！！！")

    def get_sex(self):
        return self.__sex

    def set_username(self, username):
        if username == "":
            print("你就是空白？")
        else:
            self.__username = username

    def get_username(self):
        return self.__username


class workers(person):

    def work(self):
        print("我是工人，我叫%s,性别%s,今年%d岁了,我正在干活" % (super().get_username(), super().get_sex(), super().get_age()))


class student(person):
    __number = ""

    def set_number(self, number):
        if number == "":
            print("学号非法！")
        else:
            self.__number = number

    def get_number(self):
        return self.__number

    def learn(self):
        print("我是学生,我叫%s,性别%s,今年%d岁了,这是我的学号:%s,我正在学习" % (self.get_username(), super().get_sex(),
                                                         super().get_age(), self.__number))

    def sing(self):
        print("我是学生,我叫%s,性别%s,今年%d岁了,这是我的学号:%s,我正在唱歌" % (self.get_username(), super().get_sex(),
                                                         super().get_age(), self.__number))


work = workers()
stu = student()
work.set_username("张三")
work.set_sex('男')
work.set_age(30)
stu.set_username("小小")
stu.set_sex("女")
stu.set_age(12)
stu.set_number(16512389456)
work.work()
stu.learn()
stu.sing()