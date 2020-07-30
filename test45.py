class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b
  def __str__(self):
      return f"{self.a} and {self.b}"

  def display(self):
      print(f"Values {self.a},{self.b}")

class B(A):

   def __init__(self,a,b,c):
     super().__init__(a,b)
     self.c=c

   def __str__(self):
      return f"{self.a} and {self.b} and {self.c}"

   def display(self):
      print(f"Values {self.a} ,{self.b},{self.c}")


if __name__=="__main__":
   a=A(3,4)
   b=B(5,6,7)
   print(a)
   print(b)
   print(a.__dict__)
   print(b.__dict__)
   a.display()
   b.display()


     