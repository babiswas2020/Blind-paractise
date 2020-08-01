import csv

if __name__=="__main__":
  with open("filetoday.csv",'w',newline='') as file:
      fields=['col1','col2','col3','col4']
      writer=csv.DictWriter(file,fieldnames=fields)
      writer.writeheader()
      writer.writerow({'col1':'Bapan','col2':'Dapan','col3':'Gapan','col4':'Chapan'})
      writer.writerow({'col1':'lapan','col2':'Tapan','col3':'Mapan','col4':'Sapan'})
      