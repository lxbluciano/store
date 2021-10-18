import random

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
# 空字典
bank = {
    72488604: {"username": 'luciano', 'account': 72488604, 'password': '123456', 'country': 'china', 'province': 'SD',
               'street': '74','door': 'star', 'money': 100000, 'bank_name': 'M73迪迦银行'}}

# 'F': {'account': 98835406, 'password': '1', 'country': '中国', 'porvince': '昌平', 'street': '001', 'door': '001', 'money': 0}
bank_name = "M73迪迦银行"


# 调用的函数元素是一一对应的，不是名称对应
def bank_add(account, username, password, country, province, street, door):
    if account in bank:  # 名字  重名
        return 2
    elif len(bank) >= 100:  # 大于100个用户
        return 3
    else:  # 正常添加用户
        bank[account] = {
            "username": username,
            "account": account,
            "password": password,
            "country": country,
            "province": province,
            "street": street,
            "door": door,
            "money": 0,
            "bank_name": bank_name
        }

        return 1


def Useradd():
    account = random.randint(10000000, 99999999)  # 账号随机产生的
    username = input("请输入您的姓名")
    password = input("请输入你的密码")
    print("下面请输入您的地址：")
    country = input("\t\t请输入你的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    add = bank_add(account, username, password, country, province, street, door)
    if add == 3:
        print("数据库已满，请到光之国银行开户")
    elif add == 2:
        print("用户已存在")
    elif add == 1:
        print("恭喜你添加用户成功，以下是您的账户信息：")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[account]["money"], bank_name))


def Userpass():
    print("请登录并认证")
    acc =int(input("请输入账号"))
    print(bank)
    if acc in bank:
        print("身份信息正确，登陆成功")
        mon =int(input("请输入要存入的金额"))
        bank[acc]["money"] += mon
        print("账户当前余额", bank[acc]["money"])

    else:
        print("False")

def dwon():
    print("请登录并认证")
    acc = int(input("请输入账号"))
    pas = input("请输入密码")
    mone=int(input("您要取出的金额"))
    if acc in bank:
       if pas in bank[acc]["password"]:
           if mone <=bank[acc]["money"]:
               bank[acc]["money"] -= mone
               print("取钱成功，账户余额如下")
               info = '''
                               ------------个人信息------------
                               用户名:%s
                               账号：%s
                               余额：%s
                        '''
               print(info % (
               bank[acc]["username"], acc,  bank[acc]["money"]))
           else:
               print("账户余额不足")
       else:
           print("密码不对")
    else:
        print("账户不存在")

def remove():
    acc=input("输入要转出的账号")
    accin=input("输入要转入的账号")
    passout = input("请验证转出账号密码")
    mony=int(input("输入你要转的金额"))
    if acc in bank and accin in bank:
        if passout in bank[acc]["password"]:
            if mony <= bank[acc]["money"]:
                bank[acc]["money"] -= mony
                bank[accin]["money"] += mony
                print("转账成功,现余额如下")
                info = '''
                                               ------------个人信息------------
                                               用户名:%s
                                               账号：%s
                                               密码：*****
                                               余额：%s
                        '''
                print(info % (
                    bank[acc]["username"], acc, bank[acc]["money"]))
            else:
                print("余额不足")
        else:
            print("输入的密码不对")
    else:
        print("账号不对")

def find():
    acc = int(input("请输入要查询的账号"))
    pas = input("请输入密码")
    if acc in bank:
        if pas in bank[acc]["password"]:
            print("查询用户成功，以下是您的账户信息：")
            info = '''
                                ------------个人信息------------
                                用户名:%s
                                账号：%s
                                密码：*****
                                国籍：%s
                                省份：%s
                                街道：%s
                                门牌号：%s
                                余额：%s
                                开户行名称：%s
                            '''
            # 每个元素都可传入%
            print(info % (bank[acc]["username"], acc,bank[acc]["country"],bank[acc]["province"],bank[acc]["street"],bank[acc]["door"],bank[acc]["money"], bank_name))
        else:
            print("密码错误")
    else:
        print("该用户不存在")


while True:
    index = int(input("请输入您的操作"))
    if index == 1:
        Useradd()
        print(bank)
    elif index == 2:
        Userpass()
    elif index==3:
        dwon()
    elif index==4:
        remove()
    elif index==5:
        find()
    else:
        break
# def  add():
#     a=int(input("数字"))
#     b=int(input("数字2"))
#     c=a+b
#     if c==10:
#         return 1
# if add(5,5) ==1:
#     print("成功")
