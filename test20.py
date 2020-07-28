from abc import ABC

class A(ABC):
   def __init__(self,a,b):
       self.a=a
       self.b=b
   from abc import abstractmethod
   @abstractmethod
   def display(self):
       pass

class C(A):
   def __init__(self,a,b,c):
       A.__init__(self,a,b)
       self.c=c

   def display(self):
      return f"{self.a} and {self.b}"

if __name__=="__main__":
   c=C(4,5,6)
   print(c.__dict__)
   print(c.display())


   