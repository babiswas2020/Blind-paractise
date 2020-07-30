class A:
   def __init__(self,a,b):
       self.a=a
       self.b=b

   def __str__(self):
      return f"{self.a} and {self.b}"

   def __call__(self,func):
       def wrapper(*args):
          print("Wrapper executed")
          return func(*args)
       return wrapper

@A(1,2)
def function(*args):
    for i in args:
      print(i)

if __name__=="__main__":
  function(5,6,7)
   
       
 