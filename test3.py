from concurrent.futures import ProcessPoolExecutor
from time import sleep
import random
import concurrent.futures
from queue import Queue


def task(str1):
   print(f"Obtained task {str1}")
   sleep(2)
   print(f"Completed task {str1}")
   return f"Task {str1} finished"

if __name__=="__main__":
   queue=Queue()
   for i in range(10):
      queue.put(task)
   with ProcessPoolExecutor() as executor:
      futures=[executor.submit(task,"task "+str(i)) for i in range(10)]
      done,not_done=concurrent.futures.wait(futures,return_when=concurrent.futures.FIRST_COMPLETED)
      print("Displayed by done method")
      for future in done:
         print(future.result())
      print("Displayed by future list")
      for fut in futures:
          print(fut.result())


   
   