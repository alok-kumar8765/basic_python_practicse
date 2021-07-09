#Working with CVS
import csv

#open the file
data=open('example.csv',encoding='utf-8')
#csv.reader
csv_data=csv.reader(data)
#reformatted into python obj (list of list)
data_line=list(csv_data)
#print(data_line)

#check first row item
print(data_line[0])

#check number of rows 
print(len(data_line))

#print few rows in list of list
#for line in data_line[1:5]:
    #print(line)

#Extract any single row
#print(data_line[10])

#Extract any single value of any line
#print(data_line[20][3])

#Extracting all email in table
all_email=[]
for x in data_line[1:15]:
    all_email.append(x[3])
#print(all_email)

#get a full name from first and last name
full_name=[]
for line in data_line[1:]:
        full_name.append(line[1]+' '+ line[2])
#print(full_name)

#write csv file
file_to_output = open('save_file.csv','w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerow(['a','b','c'])
file_to_output.close()

#save multiple list
file_to_output = open('save_file.csv','w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
csv_writer.writerows([['1','2','3'],['4','5','6']])
file_to_output.close()

#appending on existing file
f = open('to_save_file.csv','a',newline='')
csv_writer = csv.writer(f)
csv_writer.writerow(['new','new','new'])
f.close()