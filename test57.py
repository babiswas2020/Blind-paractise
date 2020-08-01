import asyncio
import time

async def func():
   print("Beginning Func")
   await asyncio.sleep(2)
   print("Completed func")

async def main():
  task1=asyncio.create_task(func())
  task2=asyncio.create_task(func())
  await task1
  await task2

async def main1():
   await func()
   await func()

if __name__=="__main__":
  time1=time.time()
  asyncio.run(main1())
  print(f"time is {time.time()-time1}")