import csv

if __name__=="__main__":
   with open("filetoday.csv",'r') as file:
      reader=csv.DictReader(file)
      for row in reader:
         print(row['col1'],row['col2'],row['col3'],row['col4'])
