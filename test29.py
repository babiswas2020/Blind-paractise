from contextlib import contextmanager

@contextmanager
def test(filename):
    try:
       file=open(filename,'w')
       yield file
    finally:
       if file:
         file.close()

if __name__=="__main__":
  with test("hello200.txt") as f:
       f.write("hello200\n")
       f.write("hello3000\n")
       f.write("hello5000\n")

      