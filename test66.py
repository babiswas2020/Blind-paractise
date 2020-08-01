import asyncio
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import time

def func():
  print("Begining func")
  time.sleep(4)
  print("Completed func")
  return "Finished func"

def task():
   executor=ThreadPoolExecutor()
   return executor

async def another_task():
   print("Beginning another task")
   await asyncio.sleep(2)
   print("Completed task")
   return "Another task Completed"
  
async def main():
  return await asyncio.gather(task().submit(func),asyncio.ensure_future(another_task))

if __name__=="__main__":
  asyncio.run(main())

   


    

