from concurrent.futures import ThreadPoolExecutor
from time import sleep
from queue import Queue
import concurrent.futures


def task(str1):
   print(f"Obtained task {str1}")
   sleep(2)
   print(f"Completed task {str1}")
   return f"Task {str1} finished"


if __name__=="__main__":
  queue=Queue()
  for i in range(10):
      queue.put(task)
  with ThreadPoolExecutor() as executor:
       futures=[executor.submit(queue.get(),"task "+str(i)) for i in range(10)]
       done,not_done=concurrent.futures.wait(futures,return_when=concurrent.futures.ALL_COMPLETED)
       for fut in done:
          print(fut.result())

           
           

