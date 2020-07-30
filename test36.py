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

if __name__=="__main__":
   a=A(3,4)
   b=B(11,12)
   print(hasattr(a,'a'))
   print(hasattr(a,'b'))
   print(hasattr(b,'c'))
   print(hasattr(b,'d'))