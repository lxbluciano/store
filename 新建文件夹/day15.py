f=open(r'D:\项目\day15【异常处理】\baidu_x_system.log',mode="r+",encoding="utf-8")
date=f.readlines()

all_ip=[]
ip_cound={}
for i in date:
    ip=i.split(" ",1)
    all_ip.append(ip[0])

for d in all_ip:
    if d in ip_cound:
        ip_cound[d]+=1
    else:
        ip_cound[d]=1
print(ip_cound)
