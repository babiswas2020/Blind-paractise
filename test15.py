from itertools import islice

l=[1,2,3,4,5,6]
k=iter(l)

print("Displaying the first slice")
m=islice(k,3)
for i in m:
   print(i)


print("Displaying the second slice")
m=islice(k,3)
for i in m:
  print(i)
