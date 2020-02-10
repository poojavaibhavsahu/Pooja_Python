from threading import Thread
from time import sleep
class mythread (Thread):
    def run (self):
        for i in range(1,11,1):
            sleep(2)
            print(i)
t1=mythread()
t1.start()
t1.join()
t2=mythread()
t2.start()

