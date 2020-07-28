class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b
  def __str__(self):
      return f"{self.a} and {self.b}"

if __name__=="__main__":
   a=A(3,4)
   b=A(5,6)
   if isinstance(a,A):
      print(f"{a} is instance of A")
   if hasattr(b,'a'):
      print(f"A has {a} attribute")
   if hasattr(a,'a'):
      print(True)