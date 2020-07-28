from multiprocessing import Process
from time import sleep

def task1(str1):
   print(f"Task {str1} obtained")
   sleep(2)
   print(f"Task {str1} completed")

def task2(str1):
   print(f"Task {str1} obtained")
   sleep(2)
   print(f"Task {str1} completed")

if __name__=="__main__":
   p1=Process(target=task1,args=("task1",))
   p2=Process(target=task2,args=("task2",))
   p1.start()
   p2.start()
   p1.join()
   p2.join()

   