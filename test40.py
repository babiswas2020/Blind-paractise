import csv
from csv import DictWriter

if __name__=="__main__":
  with open("file.csv",'w',newline='') as file:
       fields=['col1','col2','col3','col4']
       writer=DictWriter(file,fieldnames=fields)
       writer.writeheader()
       writer.writerow({'col1':"hello1",'col2':"hello2",'col3':"hello3",'col4':"hello4"})
       writer.writerow({'col1':"hello10",'col2':"hello20",'col3':"hello30",'col4':"hello40"})
       writer.writerow({'col1':"hello100",'col2':"hello200",'col3':"hello300",'col4':"hello400"})
