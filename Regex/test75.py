import asyncio

async def test():
   print("Beginning test")
   await asyncio.sleep(2)
   print("Test completed")

if __name__=="__main__":
   loop=asyncio.get_event_loop()
   l=loop.run_until_complete(test())
   loop.close()

   