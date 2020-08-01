import asyncio
import time

async def task1():
   print("Beginning task1")
   await asyncio.sleep(2)
   return "Task1 Completed"

async def task2():
  print("Begining task2")
  await asyncio.sleep(2)
  return "Task2 Completed"

async def task3():
  print("Begining task3")
  await asyncio.sleep(2)
  return "Task3 completed"

async def main():
   return await asyncio.gather(task1(),task2(),task3())

if __name__=="__main__":
   time1=time.time()
   l=asyncio.run(main())
   print(l)
   print(f"{time.time()-time1}")

  