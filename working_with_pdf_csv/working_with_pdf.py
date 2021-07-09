import PyPDF2
f=open('Working_Business_Proposal.pdf','rb')
pdf_reader=PyPDF2.PdfFileReader(f)
print(pdf_reader.numPages)  #to count number of pages in pdf file


#Exctract single page text 
page_one=pdf_reader.getPage(0)
page_one_text=page_one.extractText()
#print(page_one_text)
f.close()


#adding new file to pdf 
f=open('Working_Business_Proposal.pdf','rb')
pdf_reader=PyPDF2.PdfFileReader(f)
first_page=pdf_reader.getPage(0)
pdf_writer=PyPDF2.PdfFileWriter()
print(type(first_page))
pdf_writer.addPage(first_page)
pdf_output = open("Some_New_Doc.pdf","wb")
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()

f=open('Working_Business_Proposal.pdf','rb')

pdf_text=[]
pdf_reader=PyPDF2.PdfFileReader(f)
for num in range(pdf_reader.numPages):
    page=pdf_reader.getPage(num)
    pdf_text.append(page.extractText())
print(pdf_text[1])