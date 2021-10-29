# import  pymysql
#
# con=pymysql.connect(host="localhost",user="root",password="123456",database="company")
#
# cursor=con.cursor()
# #增
# # sql="insert into t_dept values(%s,%s,%s)"
# # deptname=input("请输入部门：")
# # param=[100,deptname,'北京']
# # cursor.execute(sql,param)
# # 删
# # sql="delete from t_dept where deptno>%s"
# # param=[70]
# # cursor.execute(sql,param)
# # 改
# # sql="update t_employees set sal=sal+%s"
# # param=[1000]
# # cursor.execute(sql,param)
# # 查
# # sql="select * from t_employees where sal>%s"
# # param=[4000]
# # cursor.execute(sql,param)
# # date=cursor.fetchall()  #输出多少，all，one，many（）
# # for i in date:
# #     print(i)
# con.commit()
#
# cursor.close()
# con.close()





import pymysql

host="localhost"
user="root"
password="123456"
database="bank"

#增、删、改
def update(sql,paral):
    con=pymysql.connect(host=host,user=user,password=password,database=database)
    cursor=con.cursor()
    cursor.execute(sql,paral)
    con.commit()

    cursor.close()
    con.close()


def select(sql,param,mode="all",size=1):
    con = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute(sql,param)
    # 提取数据
    if mode=="one":
        return cursor.fetchone()
    elif mode=="all":
        return cursor.fetchall()
    elif mode=="many":
        return cursor.fetchmany(size)
    con.commit()

    cursor.close()
    con.close()




