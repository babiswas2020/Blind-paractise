class A(Exception):
  def __init__(self,name):
      self.name=name
  def __str__(self):
      return f"{self.name} occured"

if __name__=="__main__":
   try:
      print("Inside try block")
      raise A("Sudden Exception")
   except Exception as e:
      print("Inside catch block")
      print(e)