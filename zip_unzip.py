'''
p=open('New_file1.txt','w+')
p.write('This is file one')
p.close()

#let make another new file
p=open('new_file2.txt','w+')
p.write('New file two')
p.close

#Now let zip these 2 file
import zipfile

#step one crate obj to put zile
com_file=zipfile.ZipFile('com_file.zip','w')
com_file.write('new_file1.txt',compress_type=zipfile.ZIP_DEFLATED)
com_file.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)
com_file.close()

#now lets unzip files
zip_obj=zipfile.ZipFile('com_file.zip','r')
zip_obj.extractall('exctracted_content')
'''
#Let suppose we want fol zip a folder
import shutil
directory_to_zip='C:\\Users\\alokk\\OneDrive\\Documents\\GitHub\\basic_python_practicse\\.pytest_cache'
output_file='example2'
shutil.make_archive(output_file,'zip',directory_to_zip)

#unzipping
dir_for_extract_result='C:\\Users\\alokk\\OneDrive\\Documents\\GitHub\\basic_python_practicse\\example.zip'
output_file='example'

shutil.unpack_archive('example2.zip','final_unzip','zip')