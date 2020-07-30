from threading import Thread
from time import sleep
import random
from queue import Queue

def task(str1):
   print(f"Obtained task {str1}")
   sleep(2)
   print(f"Completed task {str1}")

if __name__=="__main__":
   queue=Queue()
   for i in range(10):
      queue.put(task)
   thread_pool=[Thread(target=task,args=("task "+str(i),)) for i in range(10)]
   for thread in thread_pool:
       thread.start()
   for thread in thread_pool:
       thread.join()

   
   