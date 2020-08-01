import asyncio
import time

async def task2():
   print("Begining task2")
   await asyncio.sleep(2)
   print("Completed task2")

async def task1():
   print("Begining task1")
   await asyncio.sleep(3)
   await task2()
   print("Completed task1")

if __name__=="__main__":
   asyncio.run(task1())

   