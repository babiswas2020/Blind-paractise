import asyncio


async def task():
   print("Beginning a task")
   await asyncio.sleep(3)
   print("Completed task")


async def main():
   list=[]
   for i in range(10):
      list.append(asyncio.ensure_future(task()))
   await asyncio.gather(*list)

if __name__=="__main__":
   loop=asyncio.get_event_loop()
   loop.run_until_complete(main())
   loop.close()
