###################################################
from HslCommunication import SiemensS7Net
from HslCommunication import SiemensPLCS
import time
import threading
from threading import Thread

siemens = SiemensS7Net(SiemensPLCS.S200Smart, "192.168.2.1")

if siemens.ConnectServer().IsSuccess == True:
    print ('')
    print ('连接成功 !')
    print ('')
    #print ('请按启动')
else:
    print ('')
    print ('连接失败 !')
    print ('')
    exit ()
###################################################

def step1():
    while 1:
        a=0
        b=2
        times=0
        while times<24:
            #红色
            info='Q{str_a}.{str_b}'\
                .format(str_a=a,str_b=b)
            siemens.WriteBool(info,True)
            time.sleep(0.25)
            siemens.WriteBool(info,False)
            time.sleep(0.25)
            times+=1
            b+=3
            if times==2:
                a=a+1
                b=b-6
            #绿色
            if times==4:
                a=0
                b=3
            if times==6:
                a=a+1
                b=b-6
            #蓝色
            if times==8:
                a=0
                b=4
            if times==10:
                a=a+1
                b=b-6
            #黄色
            if times==12:
                a=0
                b=2
            if times==14:
                a=a+1
                b=b-6
            #紫色
            if times==16:
                a=0
                b=2
            if times==18:
                a=a+1
                b=b-6
            #青色
            if times==20:
                a=0
                b=3
            if times==22:
                a=a+1
                b=b-6

def step2():
    while 1:
        a=0
        b=3
        times=0
        read1 = siemens.ReadBool("Q1.7")
        if read1.Content == True:
            time.sleep(0.5)
            while times<12:
                #黄色
                info='Q{str_a}.{str_b}'\
                    .format(str_a=a,str_b=b)
                siemens.WriteBool(info,True)
                time.sleep(0.25)
                siemens.WriteBool(info,False)
                time.sleep(0.25)
                times+=1
                b+=3
                if times==2:
                    a=a+1
                    b=b-6
                #紫色
                if times==4:
                    a=0
                    b=4
                if times==6:
                    a=a+1
                    b=b-6
                #青色
                if times==8:
                    a=0
                    b=4
                if times==10:
                    a=a+1
                    b=b-6

if __name__ == '__main__':
    Thread(target = step1).start()
    Thread(target = step2).start()