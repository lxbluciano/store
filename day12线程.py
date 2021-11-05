from threading import Thread
import time

number = 500  #篮子的大小
n=0           #做了多少
ber=0         #篮子里有
sheng=0       #还有
ruzhang=0     #收入
bigen=time.perf_counter()

class chushi(Thread):
    cname = ""
    def run(self) -> None:
        global number,n,ber
        while True:
            end=time.perf_counter()
            if int(end-bigen)==30:
                n_money=n*1.5
                print("工作结束,%s今天做了%d个蛋挞,工资为%.2f" % (self.cname, n, n_money))
            if number>0:
                number -= 1
                n += 1
                ber += 1
                print("%s已经做了%d个蛋挞，篮子还剩%d的空间" % (self.cname, n, number))
            else:
                time.sleep(3)


class guke(Thread):
    gkname = ""
    def run(self) -> None:
        global number,ber,sheng,ruzhang
        money = 3000  # 钱
        num = 0  # 买到的数量
        while True:
            end=time.perf_counter()
            if int(end - bigen) == 30:
                print("%s今天抢到了%d个蛋挞，金额剩余：%d" % (self.gkname, num, money))
                break
            if money>=3 and ber>0:
               num = num+1
               number+=1
               money = money-3
               ber -= 1
               ruzhang+= 3
               print("恭喜",self.gkname,"买到了",num,"个蛋挞","剩余钱数",money,"还有",ber,"个蛋挞")
            elif money>=3 and n<=0:
                time.sleep(2)
            elif money<3:
                continue

class zongshour(Thread):

    def run(self) -> None:
        global ruzhang
        while True:
            end = time.perf_counter()
            if int(end - bigen) == 30:
                print("今天总收入：￥%d" % ruzhang)
                break



b1=chushi()
b2=chushi()
b3=chushi()
b1.name="m"
b2.name="h"
b3.name="y"

p1=guke()
p2=guke()
p3=guke()
p4=guke()
p5=guke()
p6=guke()
p7=guke()
p1.gkname="xiao"
p2.gkname="shuai"
p3.gkname="xia"
p4.gkname="xio"
p5.gkname="xao"
p6.gkname="iao"
p7.gkname="ao"

qian=zongshour()
b1.start()
b2.start()
b3.start()
p1.start()
p2.start()
p3.start()
p4.start()
p5.start()
p6.start()
p7.start()
qian.start()
