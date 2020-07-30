import csv
from csv import DictWriter

if __name__=="__main__":
  with open("test1.csv",'w',newline='') as file:
      fields=['column1','column2','column3']
      writer=DictWriter(file,fieldnames=fields)
      writer.writeheader()
      writer.writerow({'column1':'hello','column2':'bello','column3':'mello'})

