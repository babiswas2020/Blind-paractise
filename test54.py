import asyncio

async def task1():
   print("Task1 Started")
   await asyncio.sleep(2)
   print("Task1 completed")
   return 1

async def task2():
   print("Task2 started")
   await asyncio.sleep(2)
   print("Task2 completed")
   return 2

async def task3():
   print("Task3 started")
   await asyncio.sleep(2)
   print("Task3 completed")
   return 3

async def main():
  return await asyncio.gather(task1(),task2(),task3())


if __name__=="__main__":
  loop=asyncio.get_event_loop()
  l=loop.run_until_complete(main())
  loop.close()
  print("Displaying results")
  print(l)

  