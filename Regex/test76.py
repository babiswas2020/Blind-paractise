import re
NameAge="""Bapan is 22 and Shalini is 12 Priyanka is 32 and Srikanth is 13"""
ages=re.findall(r'\d+',NameAge)
print(ages)