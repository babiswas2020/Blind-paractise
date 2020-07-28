from multiprocessing import Process
from time import sleep
import random
from queue import Queue

def task(str1):
   print(f"{str1} task obtained")
   sleep(2)
   print(f"{str1} task completed")

if __name__=="__main__":
   queue=Queue()
   for i in range(10):
      queue.put(task)
   process_pool=[]
   for i in range(10):
      process_pool.append(Process(target=queue.get(),args=("task "+str(i),)))
   for process in process_pool:
       process.start()
   for process in process_pool:
       process.join()



