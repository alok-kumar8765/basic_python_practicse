#Grab google drive link from csv
import csv
from typing import Pattern
data=open('Exercise_Files/find_the_link.csv',encoding='UTF-8')
csv_data=csv.reader(data)
data_line=list(csv_data)
#print(data_line)
link_srt=''
for row_num,data in enumerate(data_line):
    link_srt+=data[row_num]
print(link_srt)

#Download from google driveand find phone number
import PyPDF2
f=open('Exercise_Files/Find_the_Phone_Number.pdf','rb')
pdf=PyPDF2.PdfFileReader(f)
print(pdf.numPages)
import re
pattern=r'\d{3}.\d{3}.\d{4}'
all_text=''
for n in range(pdf.numPages):
    page=pdf.getPage(n)
    page_text=page.extractText()
    all_text=all_text+' '+page_text
#print(all_text)
for match in re.findall(pattern,all_text):
    print(match)
print(all_text[41790:41808+20])