from itertools import islice

l=[1,2,3,4,5,6]
k=iter(l)

m=islice(k,2)
print(m)
for i in m:
  print(i)
o=islice(k,2)
for i in o:
   print(i)
o=islice(k,2)
for i in o:
   print(i)




