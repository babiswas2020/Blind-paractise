class A:
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def __str__(self):
       return f"{self.a} and {self.b}"

   def __call__(self,func):
      def wrapper(*args):
          return func(*args)
      return wrapper

def func(*args):
   for i in args:
      print(i)

if __name__=="__main__":
   a=A(4,5)
   print(a)
   wrap=a(func)
   wrap(1,2,3,4)
