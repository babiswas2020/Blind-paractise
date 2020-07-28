from multiprocessing import Array
from time import sleep
from multiprocessing import Process

def task(l,arr):
   for i,val in enumerate(l):
      arr[i]=val*val
   print(arr[:])

if __name__=="__main__":
   arr=Array('i',5)
   l=[1,2,3,4,5]
   p=Process(target=task,args=(l,arr))
   p.start()
   p.join()
   print(arr[:])

   
      