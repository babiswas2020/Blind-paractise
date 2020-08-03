import csv

if __name__=="__main__":
   with open("Test35.csv",'w') as file:
       fields=['col1','col2','col3','col4']
       writer=csv.DictWriter(file,fieldnames=fields)
       writer.writeheader()
       writer.writerow({'col1':"Bello",'col2':"Mello",'col3':"Tello",'col4':"Nello"})
       writer.writerow({'col1':"Tello",'col2':"Gello",'col3':"Chillo",'col4':"Dillo"})

        