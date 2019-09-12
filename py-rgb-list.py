###################################################
from HslCommunication import SiemensS7Net
from HslCommunication import SiemensPLCS
import time
import threading
from threading import Thread

siemens = SiemensS7Net(SiemensPLCS.S200Smart, "192.168.2.1")
if siemens.ConnectServer().IsSuccess == True:
    print ('连接成功 !')
else:
    print ('连接失败 !')
    exit ()
###################################################

while 1:
        a=0
        b=2
        j=0
        k=8
        m=0
        n=8
        x=0
        y=8
        times=0
        while times<31:
            info1='Q{str_a}.{str_b}'\
                .format(str_a=a,str_b=b)
            info2='Q{str_j}.{str_k}'\
                .format(str_j=j,str_k=k)
            info3='Q{str_m}.{str_n}'\
                .format(str_m=m,str_n=n)
            info4='Q{str_x}.{str_y}'\
                .format(str_x=x,str_y=y)
            siemens.WriteBool(info1,True)
            siemens.WriteBool(info2,True)
            siemens.WriteBool(info3,True)
            siemens.WriteBool(info4,True)
            time.sleep(0.2)
            siemens.WriteBool(info1,False)
            siemens.WriteBool(info2,False)
            siemens.WriteBool(info3,False)
            siemens.WriteBool(info4,False)
            time.sleep(0.2)
            times+=1
            if times <29:
                b+=3
            if 12<times<29:
                k+=3
            if 24<times<29:
                n+=3
            timelist_ab1=[2,6,10,14,18,22,26]
            timelist_ab2=[4,20]
            timelist_ab3=[12,16,24,28]
            timelist_ab4=[8]
            timelist_ab5=[29,30]
            if times in timelist_ab1:
                a+=1
                b-=6
            if times in timelist_ab2:
                a=0
                b=3
            if times in timelist_ab3:
                a=0
                b=2
            if times in timelist_ab4:
                a=0
                b=4
            if times in timelist_ab5:
                a=0
                b+=1

            timelist_jk1=[14,18,22,26]
            timelist_jk2=[16,20]
            timelist_jk3=[12,24]
            timelist_jk4=[28]
            timelist_jk5=[29,30]
            if times in timelist_jk1:
                j+=1
                k-=6
            if times in timelist_jk2:
                j=0
                k=4
            if times in timelist_jk3:
                j=0
                k=3
            if times in timelist_jk4:
                j=0
                k=5
            if times in timelist_jk5:
                j=0
                k+=1

            timelist_mn1=[26]
            timelist_mn2=[28]
            timelist_mn3=[29,30]
            timelist_mn4=[24]
            if times in timelist_mn1:
                m+=1
                n-=6
            if times in timelist_mn2:
                m=1
                n=2
            if times in timelist_mn3:
                m=1
                n+=1
            if times in timelist_mn4:
                m=0
                n=4

            timelist_xy1=[28]
            timelist_xy2=[29,30]
            if times in timelist_xy1:
                x=1
                y=5
            if times in timelist_xy2:
                x=1
                y+=1