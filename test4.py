from abc import ABC,abstractmethod

class A(ABC):
   def __init__(self,a,b):
       self.a=a
       self.b=b
   @abstractmethod
   def display(self):
      pass

class B(A):
   def display(self):
      print(self.__dict__)

if __name__=="__main__":
   b=B(5,6)
   print(b.__dict__)
   b.display()

