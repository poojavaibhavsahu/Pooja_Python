from threading import  *
class myThread(Thread):
    def run(self):
        print("Thread is running")
        print("thread name is",current_thread().getName())
t1=myThread()
t1.setName("pooja")
t1.start()
t2=myThread()
t2.start()
