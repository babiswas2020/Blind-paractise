from concurrent.futures import ProcessPoolExecutor
from time import sleep
from queue import Queue
import random
import concurrent.futures

def task(str1):
    print(f"Task recieved {str1}")
    sleep(2)
    print(f"Completed task {str1}")

if __name__=="__main__":
   queue=Queue()
   task_list=[queue.put(task) for i in range(10)]
   with ProcessPoolExecutor() as executor:
       futures=[executor.submit(queue.get(),"task "+str(i)) for i in range(10)]
       done,not_done=concurrent.futures.wait(futures,return_when=concurrent.futures.ALL_COMPLETED)
       for fut in done:
          print(fut.result())

       
       
    
    