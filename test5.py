from concurrent.futures import ThreadPoolExecutor
from time import sleep
import random
import concurrent.futures
from queue import Queue

def task(str1):
   print(f"{str1} task obtained")
   sleep(3)
   print(f"Completed task {str1}")
   return f"Task {str1} done"

if __name__=="__main__":
   queue=Queue()
   for i in range(10):
      queue.put(task)
   with ThreadPoolExecutor() as executor:
      futures=[executor.submit(queue.get(),"task "+str(i)) for i in range(10)]
      done,not_done=concurrent.futures.wait(futures,return_when=concurrent.futures.ALL_COMPLETED)
      for future in done:
        print(future.result())

