import random
from demo import select
from demo import update

print("***********************")
print("*   中国工商银行        *")
print("***********************")
print("*     1、开户          *")
print("*     2、存钱          *")
print("*     3、取钱          *")
print("*     4、转账          *")
print("*     5、查询          *")
print("*     6、再见          *")
print("***********************")

bank_name = "中国工商银行"
def getCount():
    account =random.randint(10000000, 99999999)
    return account

def bank_add(username, password, country, province, street, door, money):
    sql="select count(*) from users"
    param=[]
    data=select(sql,param)
    if len(data)>=100:
        return 3

    sql1="select * from users where username=%s"
    param1=[username]
    data=select(sql1,param1)
    if len(data) !=0:
        return 2

    sql2="insert into users value(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    param2=[getCount(),username,password,country,province,street,door,money,bank_name]
    update(sql2,param2)
    return 1


def Useradd():
    username = input("请输入您的姓名")
    password = int(input("请输入你的密码"))
    country = input("\t\t请输入你的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    money=int(input("请输入金额"))
    add = bank_add(username, password, country, province, street, door,money)
    if add == 3:
        print("数据库已满，请到光之国银行开户")
    elif add == 2:
        print("用户已存在")
    elif add == 1:
        print("开户成功")

#存钱
def Userpass():
    print("请登录并认证")
    acc =int(input("请输入账号"))
    sql="select * from users where account=%s"
    param = [acc]
    data = select(sql, param)
    print(data)
    if len(data)!=0:
        print("身份信息正确，登陆成功")
        mon =int(input("请输入要存入的金额"))
        sql1="update users set money=money+%s where account=%s"
        param1=[mon,acc]
        update(sql1,param1)
        sql2 = "select money from users where account=%s"
        param2 = [acc]
        m1=select(sql2, param2)
        print("账户当前余额", m1[0][0])

    else:
            print("False")
#取钱
def dwon():
    print("请登录并认证")
    acc = int(input("请输入账号"))
    pas = input("请输入密码")
    sql = "select * from users where account=%s"
    param = [acc]
    data = select(sql, param)
    print(data)
    if len(data) != 0:
            if pas!=data[0][2]:
                print("身份信息正确，登陆成功")
                mone = int(input("您要取出的金额"))
                if mone<data[0][7]:
                    sql1 = "update users set money=money-%s where account=%s"
                    param1 = [mone, acc]
                    update(sql1, param1)
                    sql2 = "select money from users where account=%s"
                    param2 = [acc]
                    m1 = select(sql2, param2)
                    print("账户当前余额", m1[0][0])

                else:
                    print("账户余额不足")
            else:
                print("密码不对")
    else:
        print("账户不存在")

def remove():
    acc = int(input("请输入转出账号"))
    accin = int(input("输入要转入的账号"))
    passout = input("请验证转出账号密码")
    sql = "select * from users where account=%s"
    param = [acc]
    data = select(sql, param)
    sql1 = "select * from users where account=%s"
    param1 = [accin]
    data1 = select(sql, param1)
    print(data,data1)
    if len(data) != 0 and len(data1) !=0:
            if passout!=data[0][2]:
                print("身份信息正确，登陆成功")
                mony = int(input("您要转出的金额"))
                if mony<data[0][7]:
                    sql2 = "update users set money=money-%s where account=%s"
                    param2 = [mony, acc]
                    update(sql2, param2)
                    sql4 = "update users set money=money+%s where account=%s"
                    param4 = [mony, accin]
                    update(sql4, param4)
                    sql3 = "select money from users where account=%s"
                    param3 = [accin]
                    m1 = select(sql3, param3)
                    print("账户当前余额", m1[0][0])

                else:
                    print("账户余额不足")
            else:
                print("密码不对")
    else:
        print("账户不存在")

def find():
    acc = int(input("请输入账号"))
    passout = input("请验证密码")
    sql = "select * from users where account=%s"
    param = [acc]
    data = select(sql, param)
    if len(data) != 0:
            if passout!=data[0][2]:
                print("身份信息正确，登陆成功")
                print("您的信息是",data)
            else:
                print("密码不对")
    else:
        print("账户不存在")

while True:
    index = int(input("请输入您的操作"))
    if index == 1:
        Useradd()
    elif index == 2:
        Userpass()
    elif index==3:
        dwon()
    elif index==4:
        remove()
    elif index==5:
        find()
    else:
        print("感谢您的使用，欢迎下次光临")
        break