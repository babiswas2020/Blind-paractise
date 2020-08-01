import asyncio
import time

async def task1():
   print("Beginning task1")
   await asyncio.sleep(2)
   print("Completed task1")

async def task2():
   print("Beginning task2")
   await asyncio.sleep(2)
   print("Completed task2")

async def task3():
   print("Beginning task3")
   await asyncio.sleep(2)
   print("Completed task3")


async def main():
   task=[]
   task.append(asyncio.ensure_future(task1()))
   task.append(asyncio.ensure_future(task2()))
   task.append(asyncio.ensure_future(task3()))
   return await asyncio.gather(*task)

if __name__=="__main__":
   loop=asyncio.get_event_loop()
   loop.run_until_complete(main())
   loop.close()

   