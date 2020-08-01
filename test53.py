import asyncio

async def routine():
   print("Started Routine")
   await asyncio.sleep(2)
   print("Completed task")

async def main():
   task=[]
   for i in range(10):
      task.append(asyncio.ensure_future(routine()))
   await asyncio.gather(*task)

if __name__=="__main__":
   loop=asyncio.get_event_loop()
   loop.run_until_complete(main())
   loop.close()



   