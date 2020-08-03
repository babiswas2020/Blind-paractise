import requests
import re

def fetch_page(url):
   response=requests.get(url)
   if response.status_code!=200:
       raise Exception
   else:
       return response.text

if __name__=="__main__":
   text=fetch_page("https://regexone.com/references/python")
   print(text)
