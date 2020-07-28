class A:
   def __init__(self,filename):
       self.name=filename
   def __enter__(self):
       self.file=open(self.name,'w')
       return self.file
   def __exit__(self,x,y,z):
       if self.file:
          self.file.close()

if __name__=="__main__":
   with A("hello100.txt") as f:
        f.write("Hello")
        f.write("Hi")
        f.write("Bye")
