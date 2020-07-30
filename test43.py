def function(cls):
   def wrapper(*args):
      def func(self,a,b):
         return a+b
      setattr(cls,'add',func)
      return cls(*args)
   return wrapper

@function
class A:
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def __str__(self):
       return f"{self.a} and {self.b}"

if __name__=="__main__":
   a=A(3,4)
   print(a.__dict__)
   print(a)
   print(a.add(5,6))

