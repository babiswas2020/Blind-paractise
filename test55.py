import asyncio

async def task1():
   print("Begin task1")
   print("Completed task1")

async def task2():
   print("Begin task2")
   await asyncio.sleep(4)
   await task1()
   print("Completed task2")

async def task3():
   print("Task3 begin")
   await asyncio.sleep(2)
   print("Completed task3")

async def main():
   return await asyncio.gather(task2(),task3())


if __name__=="__main__":
  loop=asyncio.get_event_loop()
  loop.run_until_complete(main())
  loop.close()
