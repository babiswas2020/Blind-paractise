import csv
from csv import DictWriter

if __name__=="__main__":
   with open("test2.csv",'w',newline='') as file:
       field=['col1','col2','col3']
       writer=DictWriter(file,fieldnames=field)
       writer.writeheader()
       for i in range(10):
          writer.writerow({'col1':'hello','col2':'bello','col3':'mello'})
