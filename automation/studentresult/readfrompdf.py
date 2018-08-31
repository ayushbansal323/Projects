# importing required modules
import PyPDF2,xlwt
 
# creating a pdf file object
pdfFileObj = open('input.pdf', 'rb')
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
text = ["a"] 
# printing number of pages in pdf file
print(pdfReader.numPages)
 
# creating a page object
c=pdfReader.numPages
for i in range(c):
	pageObj = pdfReader.getPage(i)
	text.append(pageObj.extractText())
 
# extracting text from page
print(text)
 
# closing the pdf file object
pdfFileObj.close()

workbook = xlwt.Workbook() 
 
sheet = workbook.add_sheet("Sheet Name")
 
# Specifying style
style = xlwt.easyxf('font: bold 1')
 
# Specifying column
sheet.write(0, 0, 'SAMPLE', style)
workbook.save("sample.xls")
