from threading import Thread
class myThread(Thread):
    def run(self) :
        num=5
        for i in range(1,10,1):
            mul=num*i
            print(num,"*",i,"=",mul)


t1=myThread()
t1.start()
from threading import Thread
class myThread(Thread):
    def run(self) :
        num=6
        for i in range(1,10,1):

            mul=num*i
            print(num,"*",i,"=",mul)


t1=myThread()
t1.start()
t1.join()
t2=myThread()
t2.start()