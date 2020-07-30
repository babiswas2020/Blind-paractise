class A:
   def __init__(self,a,b):
      self.a=a
      self.b=b

   def __str__(self):
      return f"{self.a} and {self.b}"

   @property
   def set_a(self):
       return self.a
   @property
   def set_b(self):
       return self.b
   @set_a.setter
   def set_a(self,a):
       self.a=a
   @set_b.setter
   def set_b(self,b):
       self.b=b

if __name__=="__main__":
   a=A(5,6)
   print(a.__dict__)
   print(a.set_a)
   print(a.set_b)
   a.set_a=12
   a.set_b=13
   print(a.__dict__)

   