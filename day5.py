# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# for key in dict:
#     print(key)
# for key in dict:
#     print(dict[key])
# dict["k4"]="v4"
# print(dict)


# Friuts = {
# 	'苹果':12.3,
# 	'草莓':4.5,
#     '香蕉':6.3,
#     '葡萄':5.8,
#     '橘子':6.4,
#     '樱桃':15.8
#     }
# info = {
#     '小明': {
#         'fruits': {'苹果':4, '草莓':13, '香蕉':10},
#         'money':{}
#
#     },
#     '小刚': {
#         'fruits': {'葡萄':19, '橘子':12, '樱桃':30},
#         'money':{}
#     }
# }
# a = (Friuts['苹果'] * info['小明']['fruits']['苹果'] + Friuts['草莓'] * info['小明']['fruits']['草莓'] + Friuts['香蕉'] *
#           info['小明']['fruits']['香蕉'])
# b = (Friuts['葡萄'] * info['小刚']['fruits']['葡萄'] + Friuts['橘子'] * info['小刚']['fruits']['橘子'] + Friuts['樱桃'] *
#             info['小刚']['fruits']['樱桃'])
# info['小明']['money']={a}
# info['小刚']['money']={b}
# print(info)

#
# lucia=input("输入列表")
# print(lucia)
# n=0
# m=0
# v=0
# for by in lucia:
#     if by == 21:
#         n+=1
#     elif by == 56:
#         m+=1
#     elif by == 10:
#         v+=1
# print(n,m,v)
#

#
# list1 = [21] * 3
# list2 = [56] * 9
# list3 = [10] * 3
# list = list1 + list2 + list3
# print(list)
# dict = {}
# for i in list:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
# print(dict)

#有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# names = [
#     ["刘备","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
# ]
# a={}
# for i in names:
#     if i[0] not in a.keys():
#         a[i[0]]={"年龄":i[1],"性别":i[2],"编号":i[3],"公司":i[4],"薪资":i[5],"部门":i[6]}
# print(a)

