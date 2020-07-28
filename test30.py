class A:
   def __init__(self,a,b):
      self.a=a
      self.b=b
   def __str__(self):
      return f"{self.a} and {self.b}"
   def __add__(self,other):
       if isinstance(other,A):
          self.a=self.a+other.a
          self.b=self.b+other.b
          return self


if __name__=="__main__":
   a=A(3,4)
   b=A(5,6)
   print(a+b)
   a=A(5,6)
   b=A(7,8)
   print(a+b)

