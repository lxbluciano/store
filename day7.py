import xlrd

wb = xlrd.open_workbook(filename=r"D:\项目\day07\任务\2020年每个月的销售情况.xls",encoding_override=True)
yifu = ["羽绒服", "T血", "衬衫", "风衣", "牛仔裤", "皮衣", "皮草", "小西装", "棉衣", "卫衣", "铅笔裤", "休闲裤", "马甲"]
jidu = [["1月", "2月", "12月"], ["3月", "4月", "5月"], ["6月", "7月", "8月"], ["9月", "10月", "11月"]]

pay_sum = 0
#总销售额
for j in range(12):
    st = wb.sheet_by_index(j)
    rows = st.nrows
    cols = st.ncols
    for  i  in range(1,rows):
        data = st.row_values(i)
        pay_sum = pay_sum + data[2]*data[4]
print("总销售额",round(pay_sum))

#每件衣服的销售（件数）占比

for h in yifu:
    num_zf = 0
    number = 0
    for j in range(12):
        st = wb.sheet_by_index(j)
        rows = st.nrows
        cols = st.ncols
        for  i  in range(1,rows):
            data = st.row_values(i)
            number = number + data[4]  # 年销售总量
            if data[1]==h:
                num_zf = num_zf + data[4]
    print(h,"的销售（件数）占比",num_zf/number*100,"%")
print("销售总量",int(number))

#每件衣服的月销售占比

# yue=str(input("请输入你想要查看的月份"))
# for h in yifu:
#     num_zf = 0
#     number = 0
#     st = wb.sheet_by_name(yue)
#     rows = st.nrows
#     cols = st.ncols
#     for  i  in range(1,rows):
#          data = st.row_values(i)
#          number = number + data[2]*data[4]  # 年销售总量
#          if data[1]==h:
#             num_zf = num_zf + data[2]*data[4]
#     print(h,"的销售占比",num_zf/number*100,"%")
# print("该月销售额",int(number))
#

#每件衣服的销售额占比
#
# for h in yifu:
#     num_zf = 0
#     for j in range(12):
#         st = wb.sheet_by_index(j)
#         rows = st.nrows
#         cols = st.ncols
#         for  i  in range(1,rows):
#             data = st.row_values(i)
#             if data[1]==h:
#                 num_zf = num_zf + data[2]*data[4]
#     print(h,"的销售占比",round(num_zf/pay_sum*100),"%")


#最畅销的衣服是那种

list1={}
for k in yifu:
    sum2 = 0
    for i in range(12):
        sheet = wb.sheet_by_index(i)
        rows = sheet.nrows#获取多少行
        cols = sheet.ncols#获取多少列
        for j in range(1,rows):
            data = sheet.row_values(j)
            if data[1] == k:
                sum2 = sum2 + data[4]
    list1[k] = sum2
i = max(list1, key=lambda x:list1[x])
o = min(list1, key=lambda x:list1[x])
print("最畅销的",i,"销量最低",o)




#每个季度最畅销的衣服

list1={}
print("0.冬季 1.春季 2.夏季 3.秋季")
s = int(input("请输入你想知道的季度的序号"))
for k in yifu:
    sum2 = 0
    for i in range(12):
        sheet = wb.sheet_by_index(i)
        rows = sheet.nrows#获取多少行
        cols = sheet.ncols#获取多少列
        for j in range(1,rows):
            data = sheet.row_values(j)
            if data[1] == k:
                sum2 = sum2 + data[4]
    list1[k] = sum2
i = max(list1, key=lambda x:list1[x])
o = min(list1, key=lambda x:list1[x])
print("最畅销的",i,"最不畅销的",o)
