import asyncio

async def task1():
   print("Beginning Task1")
   await asyncio.sleep(2)
   print("Completed task1")
   return f"Task1 completed"

async def task2():
   print("Beginning Task2")
   await asyncio.sleep(2)
   await asyncio.sleep(2)
   print("Completed task2")
   return f"Task 2 completed"

async def task3():
    print("Beginning task3")
    await asyncio.sleep(2)
    await asyncio.sleep(2)
    await asyncio.sleep(2)
    print("Completed task3")
    return f"Task 3 completed"

async def main():
   task_list=[task3(),task2(),task1()]
   for task in asyncio.as_completed(task_list):
       print(f"{await task}")

if __name__=="__main__":
   loop=asyncio.get_event_loop()
   loop.run_until_complete(main())
   loop.close()

    

