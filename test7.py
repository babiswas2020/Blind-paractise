from multiprocessing import Pool

def task(args):
   sum=0
   for i in args:
      sum+=i
   return sum

def multiply(args):
   product=1
   for i in args:
      product=product*i
   return product

if __name__=="__main__":
   p=Pool(processes=5)
   data=p.map(task,[(1,2,3),(4,5,6)])
   p.close()
   print(data)
   p=Pool(processes=4)
   data=p.map(multiply,[(1,2,3,4),(1,3,4,5),(1,6,7,9),(1,3,4,5)])
   print(data)
   p.close()

