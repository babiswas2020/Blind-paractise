import asyncio

async def task1():
   print("Beginning task1")
   await asyncio.sleep(2)
   print("completing task1")

async def task2():
   print("Beginning task2")
   await asyncio.sleep(2)
   print("Completing task1")

async def task3():
   print("Beginning task3")
   await asyncio.sleep(2)
   print("Completing task3")

async def main():
   await task1()
   await task2()
   await task3()

if __name__=="__main__":
   asyncio.run(main())
