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

def step1():
    while 1:
        a=0
        b=2
        times=0
        while times<31:
            info='Q{str_a}.{str_b}'\
                .format(str_a=a,str_b=b)
            siemens.WriteBool(info,True)
            time.sleep(0.15)
            siemens.WriteBool(info,False)
            time.sleep(0.15)
            times+=1
            if times <29:
                b+=3
            timelist1=[2,6,10,14,18,22,26]
            timelist2=[4,20]
            timelist3=[12,16,24,28]
            timelist4=[8]
            timelist5=[29,30]
            if times in timelist1:
                a+=1
                b-=6
            if times in timelist2:
                a=0
                b=3
            if times in timelist3:
                a=0
                b=2
            if times in timelist4:
                a=0
                b=4
            if times in timelist5:
                a=0
                b+=1

def step2():
    while 1:
        a=0
        b=3
        times=0
        read1 = siemens.ReadBool("Q1.7")
        if read1.Content == True:
            time.sleep(0.3)
            while times<19:
                info='Q{str_a}.{str_b}'\
                    .format(str_a=a,str_b=b)
                siemens.WriteBool(info,True)
                time.sleep(0.15)
                siemens.WriteBool(info,False)
                time.sleep(0.15)
                times+=1
                if times <17:
                    b+=3
                timelist1=[2,6,10,14]
                timelist2=[4,8]
                timelist3=[12]
                timelist4=[16]
                timelist5=[17,18]
                if times in timelist1:
                    a+=1
                    b-=6
                if times in timelist2:
                    a=0
                    b=4
                if times in timelist3:
                    a=0
                    b=3
                if times in timelist4:
                    a=0
                    b=5
                if times in timelist5:
                    a=0
                    b+=1

def step3():
    while 1:
        a=0
        b=4
        times=0
        read1 = siemens.ReadBool("Q1.6")
        read2 = siemens.ReadBool("Q1.7")
        if read1.Content & read2.Content == True:
                time.sleep(0.3)
                while times<7:
                    info='Q{str_a}.{str_b}'\
                        .format(str_a=a,str_b=b)
                    siemens.WriteBool(info,True)
                    time.sleep(0.15)
                    siemens.WriteBool(info,False)
                    time.sleep(0.15)
                    times+=1
                    if times <5:
                        b+=3
                    timelist1=[2]
                    timelist2=[4]
                    timelist3=[5,6]
                    if times in timelist1:
                        a+=1
                        b-=6
                    if times in timelist2:
                        a=1
                        b=2
                    if times in timelist3:
                        a=1
                        b+=1

def step4():
    while 1:
        a=1
        b=5
        times=0
        read1 = siemens.ReadBool("Q1.5")
        read2 = siemens.ReadBool("Q1.6")
        read3 = siemens.ReadBool("Q1.7")
        if read1.Content & read2.Content & read3.Content == True:
            time.sleep(0.3)
            while times<3:
                info='Q{str_a}.{str_b}'\
                    .format(str_a=a,str_b=b)
                siemens.WriteBool(info,True)
                time.sleep(0.15)
                siemens.WriteBool(info,False)
                time.sleep(0.15)
                times+=1
                timelist1=[1,2]
                if times in timelist1:
                    b+=1

if __name__ == '__main__':
    Thread(target = step1).start()
    Thread(target = step2).start()
    Thread(target = step3).start()
    Thread(target = step4).start()