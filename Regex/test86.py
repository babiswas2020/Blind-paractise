import asyncio

async def task1():
   print("Beginning task1")
   await asyncio.sleep(2)
   print("Completing task1")

async def task2():
  print("Begining task2")
  await asyncio.sleep(2)
  print("Completing task2")

async def main():
    task_1=asyncio.create_task(task1())
    task_2=asyncio.create_task(task2())
    await task_1
    await task_2

if __name__=="__main__":
   asyncio.run(main())
