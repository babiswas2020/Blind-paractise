from multiprocessing import Array
from multiprocessing import Process
from time import sleep


def task(str1,arr):
    print(f"Obtained task {str1}")
    for i in range(4):
       arr[i]=i+1

if __name__=="__main__":
   arr=Array('i',4)
   p1=Process(target=task,args=("task 1",arr,))
   p1.start()
   p1.join()
   print(arr[:])


