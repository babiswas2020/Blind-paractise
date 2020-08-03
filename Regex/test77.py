import re
from contextlib import contextmanager

@contextmanager
def file_write(name):
   try:
      file1=open(name,'w')
      yield file1
   finally:
      if file1:
         file1.close()

@contextmanager
def file_read(name):
   try:
      file1=open(name,'r')
      yield file1
   finally:
      if file1:
         file1.close()

def find_warning_message(str1):
    with file_write("warning.txt") as file:
         str2=re.findall(r'W\w+ing:\s+[\w+\s+]+[\":\s+][\w+\s+\.+\\]+[\"\.!]',str1)
         for wd in str2:
            file.write(wd+'\n')

def find_warning(str1):
    with file_write("warning1.txt") as file:
         str2=re.findall(r'W\w+ing:[\s+\w+\.!\"-\\]+[^.\s{12,13}]',str1)
         for wd in str2:
            file.write(wd+'\n')

def find_all_error(str1):
   with file_write("Error.txt") as file:
         str2=re.findall(r'Error:\s+[\w+\s+]+',str1)
         for wd in str2:
            file.write(wd+'\n')

def find_all_information(str1):
   with file_write("Info.txt") as file:
         str2=re.findall(r'Information:\s+[\w+\s+]+',str1)
         for wd in str2:
            file.write(wd+'\n')
            
if __name__=="__main__":
   with file_read("logfile.txt") as file:
        str1=file.read()
        find_warning_message(str1)
        find_all_error(str1)
        find_all_information(str1)
        find_warning(str1)



      