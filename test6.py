from multiprocessing import Pool


def add(args):
   sum=0
   for i in args:
     sum+=i
   return sum

if __name__=="__main__":
   p=Pool()
   data=p.map(add,[(1,2,3),(3,4,5)])
   p.close()
   print(data)

    