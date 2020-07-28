class A:

  def __init__(self,a,b):
      self.a=a
      self.b=b
  def __str__(self):
      return f"{self.a} and {self.b}"

class B:

   def __init__(self,c,d):
       self.c=c
       self.d=d
   def __str__(self):
      return f"{self.c} and {self.d}"

class C(A,B):

   def __init__(self,a,b,c):
       A.__init__(self,a,b)
       B.__init__(self,a,b)
       self.c=c

   def __str__(self):
       return f"{self.a},{self.b} and {self.c}"

if __name__=="__main__":
   c=C(3,4,5)
   print(c)
   print(c.__dict__)

