import asyncio

async def routine():
   print("Beginning task")
   await asyncio.sleep(2)
   print("Completed task")


if __name__=="__main__":
   loop=asyncio.get_event_loop()
   loop.run_until_complete(routine())
   loop.close()
