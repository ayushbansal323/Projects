# importing required modules
import PyPDF2,xlwt
import sys

class run:
	# creating a pdf file object
	def __init__(self,argument):
		self.texts=["*"]
		self.input = argument[1]
		self.output = argument[2]
		self.pdfFileObj = open(self.input, 'rb')
		self.lenOfSeatNumber = 10 
		self.SGPAgap = 2
		self.workbook = xlwt.Workbook() 
		self.sheet = self.workbook.add_sheet("RESULT")
		self.style = xlwt.easyxf('font: bold 1')
		self.rowCount=1
		self.colCount=0
		self.year=argument[3][0].upper()
		self.subMarksGap=7


	def pdf2excel(self):
		
		pdfReader = PyPDF2.PdfFileReader(self.pdfFileObj)		# creating a pdf reader object
		totalPages = pdfReader.numPages
		for pageNo in range(totalPages):
			counter=0
			pageObj = pdfReader.getPage(pageNo)
			texts=pageObj.extractText().split(' ')
			new_text = list(filter(lambda x:(x != "" ),texts))
			new_texts = list(filter(lambda x:(x != "*" ),new_text))
			for text in new_texts:
				text = text.upper()
				if len(text) == self.lenOfSeatNumber and text.startswith(self.year) and text[self.lenOfSeatNumber - 1].isdigit() :
					self.sheet.write(self.rowCount, self.colCount, text, self.style)
					self.colCount = self.colCount + 1 
					nameStudent = new_texts[counter+1]+ " " + new_texts[counter+2] + " " + new_texts[counter+3]
					self.sheet.write(self.rowCount, self.colCount,nameStudent , self.style)
					self.colCount = self.colCount + 1
					print(f"{text}")
				elif text == "SGPA":
					print(f"{new_texts[counter+self.SGPAgap]}")
					self.sheet.write(self.rowCount, self.colCount, new_texts[counter+self.SGPAgap].replace(',',''), self.style)
					self.colCount = 0
					self.rowCount = self.rowCount + 1
				counter = counter + 1

	def __del__(self):
		self.workbook.save(f"{self.output}.xls")

def help():
	print("to run the program type")
	print("pyton3 run.py <name of input pdf>  <name of output excel file> <Year(FE,SE,TE,BE)>")

def main():
	argument = sys.argv
	if len(sys.argv) == 4:
		if len(argument[3]) == 2:
			noofsubject
			obj=run(argument)
			obj.pdf2excel()
			del obj
	elif len(sys.argv) == 2:
		if argument[1] == '--help':
			help()

if __name__ == '__main__':
    main()