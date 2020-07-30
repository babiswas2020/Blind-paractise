class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b
  def __iter__(self):
      return self
  def __next__(self):
      if self.a>self.b:
         raise StopIteration
      item=self.a
      self.a=self.a+1
      return item

if __name__=="__main__":
   a=A(3,6)
   a.__iter__()
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))
   print(next(a))

