def func():
   m=yield
   print("Processing m")
   print(m)
   return m

if __name__=="__main__":
   try:
      m=func()
      next(m)
      m.send(24)
   except StopIteration as e:
     print(e)