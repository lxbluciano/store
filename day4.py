# 有下列人员数据库，请按要求实现
# # 姓名  年龄  性别  编号   任职公司   薪资   部门编号
# names = [
#     ["曹操","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["许褚", "45", "男", "230", "Tencent", 700 , "10"]
# ]



#
# names1 = ["曹操","56","男","106","IBM", 500 ,"50"]
# names2= ["大乔","19","女","230","微软", 501 ,"60"]
# names3= ["小乔", "19", "女", "210", "Oracle", 600, "60"]
# names4=["许褚", "45", "男", "230", "Tencent", 700 , "10"]
# print("平均薪资",(names1[5]+names2[5]+names3[5]+names4[5])/4)
# print("平均年龄",(int(names1[1])+int(names2[1])+int(names3[1])+int(names4[1]))/4)
# names5=["刘备","45","男","220","alibaba",500,"30"]
# dict1=dict(zip(["0","1","2","3","4","5","6"],names1))
# dict2=dict(zip(["0","1","2","3","4","5","6"],names2))
# dict3=dict(zip(["0","1","2","3","4","5","6"],names3))
# dict4=dict(zip(["0","1","2","3","4","5","6"],names4))
# dict5=dict(zip(["0","1","2","3","4","5","6"],names5))
# dict=[dict1,dict2,dict3,dict4,dict5]
# print(dict)
#
# a=0
# b=0
# for  item in dict:
#         if item['2'] =='男':
#             a += 1
#         else:
#             b += 1
#
# print("男生个数",a,"女生个数",b)
#
# com50,com60,com10,com30=0,0,0,0
# for c in range(len(dict)):
#     if dict[c]['6'] == '50':
#         com50 += 1
#     elif dict[c]['6'] == '60':
#         com60 += 1
#     elif dict[c]['6'] == '10':
#         com10 += 1
#     elif dict[c]['6'] == '30':
#         com30 += 1
# print("部门50的人数",com50)
# print("部门60的人数",com60)
# print("部门10的人数",com10)
# print("部门30的人数",com30)
#


# l1 = ['罗恩', '23', '35', '44']
# l2 = ['哈利', '60', '77', '68', '88', '90']
# l3 = ['赫敏', '97', '99', '89', '91', '95', '90']
# l4 = ['马尔福 ', '100', '85', '90']
# sum = 0
# s = 0
# for i in range(len(l1)):
#     if i == 0:
#         s = l1[0]
#     else:
#         sum += int(l1[i])
# print(s + "的成绩：" + str(sum))
# sum = 0
# for i in range(len(l2)):
#     if i == 0:
#         s = l2[0]
#     else:
#         sum += int(l2[i])
# print(s + "的成绩：" + str(sum))
# sum = 0
# for i in range(len(l3)):
#     if i == 0:
#         s = l3[0]
#     else:
#         sum += int(l3[i])
# print(s + "的成绩：" + str(sum))
# sum = 0
# for i in range(len(l4)):
#     if i == 0:
#         s = l4[0]
#     else:
#         sum += int(l4[i])
# print(s + "的成绩：" + str(sum))


#
# num=int(input("请输入一个数："))
# while num!=0:
#     print(num%10)
#     num=num//10

#冒泡排序

# def bubble_sort(a):
#     for i in range(1,len(a)):
#         for j in range(0,len(a)-i):
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#     return  a
#
# if __name__ == '__main__':
#     a=[5,2,4,7,9,1,3,5,4,0,6,1,3]
#     print(bubble_sort(a))
#
