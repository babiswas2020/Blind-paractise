import asyncio

async def task1():
   print("Beginning task1")
   await asyncio.sleep(2)
   print("Copmpleted task1")
   return "Task1 completed"

async def task2():
   print("Beginning task2")
   await asyncio.sleep(2)
   print("Completed task2")
   return "Task2 Completed"

async def task3():
   print("Beginning task3")
   await asyncio.sleep(2)
   print("Completed task3")
   return "Task3 Completed"


async def main():
   return await asyncio.gather(task1(),task2(),task3())

if __name__=="__main__":
   asyncio.run(main())
