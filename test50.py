import asyncio
import random

async def display():
   print("About to display")
   await asyncio.sleep(random.randint(1,3))
   print("Completed display")

if __name__=="__main__":
   loop=asyncio.get_event_loop()
   loop.run_until_complete(display())
   loop.close()

