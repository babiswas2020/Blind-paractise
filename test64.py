import asyncio

async def task1():
   print("Beginning task1")
   await asyncio.sleep(2)
   print("Completed task1")

async def task2():
  print("Beginning task2")
  await asyncio.sleep(2)
  await asyncio.sleep(2)
  print("Completed task2")

async def task3():
   print("Beginning task 3")
   await asyncio.sleep(2)
   await asyncio.sleep(2)
   await asyncio.sleep(2)
   print("Completed task3")

async def main(task_list):
   for task in asyncio.as_completed(task_list):
      await task


if __name__=="__main__":
   task_list=[task1(),task2(),task3()]
   asyncio.run(main(task_list))

   