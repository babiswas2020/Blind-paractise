import csv
from csv import DictReader

if __name__=="__main__":
   with open("file.csv",'r') as file:
      fields=['col1','col2','col3','col4']
      reader=DictReader(file,fieldnames=fields)
      for row in reader:
          print(row['col1'],row['col2'],row['col3'],row['col4'])
     