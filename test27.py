class A:
  def __new__(cls,*args,**kwargs):
     print("New method executed")
     return object.__new__(cls)
  def __init__(self,**kwargs):
      self.__dict__.update(kwargs)

if __name__=="__main__":
   a=A(m="Hello",p="bello")
   print(a.__dict__)

