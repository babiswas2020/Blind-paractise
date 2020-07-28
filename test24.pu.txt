from threading import Thread
from time import sleep
from queue import Queue


def task(str1):
   print(f"Task obtained {str1}")
   sleep(2)
   print(f"Task Completed {str1}")
   

if __name__=="__main__":
   t1=Thread(target=task,args=("task1",))
   t2=Thread(target=task,args=("task2",))
   t1.start()
   t2.start()
   t1.join()
   t2.join()


