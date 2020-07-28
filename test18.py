from multiprocessing import Pool

def task(l):
   sum=0
   for i in l:
     sum+=i
   return sum

if __name__=="__main__":
  p=Pool(processes=6)
  data=p.map(task,[(1,2,3),(4,5,6),(7,8,9),(10,11,12),(13,14,15)])
  p.close()
  print(data)
