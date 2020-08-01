import asyncio

async def task1():
   print("Beginning task1")
   await asyncio.sleep(2)
   return "Completed task1"

async def task2():
   print("Beginning task2")
   await asyncio.sleep(2)
   return "Completed task2"

async def main():
  return await asyncio.gather(task1(),task2())

if __name__=="__main__":
   loop=asyncio.get_event_loop()
   l=loop.run_until_complete(main())
   loop.close()
   print(l)

