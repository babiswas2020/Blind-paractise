from multiprocessing import Queue
from multiprocessing import Process

def task(str1,queue):
    print(f"Obtained task {str1}")
    for i in range(10):
       queue.put(i)

def task1(str2,queue):
    print(f"Obtained task {str2}")
    for i in range(10):
      print(queue.get(i))

if __name__=="__main__":
   queue=Queue()
   p1=Process(target=task,args=("task 1",queue,))
   p2=Process(target=task1,args=("task 2",queue,))
   p1.start()
   p2.start()
   p1.join()
   p2.join()
