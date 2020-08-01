import asyncio
import time

async def task1():
  print("Beginning task1")
  await asyncio.sleep(2)
  print("Completed task")
  return "Finished task1"

async def task2():
   print("Begining task2")
   await asyncio.sleep(2)
   print("Completed task")
   return "Finished task2"

async def task3():
   print("Begining task3")
   await asyncio.sleep(2)
   print("Completed task")
   return "Finished task3"

async def main():
   task_1=asyncio.create_task(task1())
   task_2=asyncio.create_task(task2())
   task_3=asyncio.create_task(task3())
   await task_1
   await task_2
   await task_3

if __name__=="__main__":
   time1=time.time()
   asyncio.run(main())
   print(f"{time.time()-time1}")


   

