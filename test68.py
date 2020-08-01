from concurrent.futures import ProcessPoolExecutor
from time import sleep
import concurrent.futures



def task1(str1):
  print(f"{str1} task is obtained")
  sleep(2)
  print(f"{str1} task completed")
  return f"Task {str1} finished"

if __name__=="__main__":
  with ProcessPoolExecutor() as executor:
      l=[executor.submit(task1,"task "+str(i)) for i in range(10)]
      done,not_done=concurrent.futures.wait(l,return_when=concurrent.futures.ALL_COMPLETED)
      for d in done:
         print(d.result())

   