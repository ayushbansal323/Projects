# importing required modules
import PyPDF2,xlwt
import sys
import csv

class run:
	# creating a pdf file object
	def __init__(self,argument,reader):
		self.texts=["*"]
		self.input = argument[1]
		self.output = argument[2]
		self.pdfFileObj = open(self.input, 'rb')
		self.lenOfSeatNumber = 10 
		self.SGPAgap = 2
		self.workbook = xlwt.Workbook() 
		self.sheet = self.workbook.add_sheet("RESULT")
		self.style = xlwt.easyxf('font: bold 1')
		self.rowCount=0
		self.colCount=0
		self.year=argument[3][0].upper()
		self.subMarksGap=7
		self.subjects=reader
		self.maxcollength=len(reader)+3
		self.coldic = {}

		self.sheet.write(self.rowCount, self.colCount, "Seat No", self.style)
		self.coldic.update({"Seat No":self.colCount})
		self.colCount = self.colCount + 1
		self.sheet.write(self.rowCount, self.colCount, "Name", self.style)
		self.coldic.update({"Name":self.colCount})
		self.colCount = self.colCount + 1
		for sub in self.subjects:
			self.sheet.write(self.rowCount, self.colCount, sub, self.style)
			self.coldic.update({sub:self.colCount})
			self.colCount = self.colCount + 1			
		self.sheet.write(self.rowCount, self.colCount, "SGPA", self.style)
		self.coldic.update({"SGPA":self.colCount})
		self.colCount = self.colCount + 1

		#print(self.coldic)
		self.rowCount=1
		self.colCount=0

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
					self.sheet.write(self.rowCount, self.coldic["Seat No"], text, self.style)
					nameStudent = new_texts[counter+1]+ " " + new_texts[counter+2] + " " + new_texts[counter+3]
					self.sheet.write(self.rowCount, self.coldic["Name"],nameStudent , self.style)
					#print(f"{text} {nameStudent}")
				elif text == "SGPA":
					#print(f"SGPA = {new_texts[counter+self.SGPAgap]}")
					self.sheet.write(self.rowCount, self.coldic["SGPA"], new_texts[counter+self.SGPAgap].replace(',',''), self.style)
					self.rowCount = self.rowCount + 1
				if text in self.subjects:
					self.sheet.write(self.rowCount, self.coldic[text], new_texts[counter + self.subMarksGap], self.style)
					#print(f"{text} marks = {new_texts[counter + self.subMarksGap] }")
				counter = counter + 1

	def __del__(self):
		self.workbook.save(f"{self.output}.xls")
		print(f"completed file saved as {self.output}.xls ")
def help():
	print("to run the program type")
	print("pyton3 run.py <name of input pdf>  <name of output excel file> <Year(FE,SE,TE,BE)>")
	print("write the subject code in subjects.txt file line by line one per line")

def main():
	argument = sys.argv
	if len(sys.argv) == 4:
		if len(argument[3]) == 2:
			file = open('subjects.txt', 'r') 
			reader= file.read().split('\n')
			reader = list(filter(lambda x:(x != "" ),reader)) 
			#print(reader)
			obj=run(argument,reader)
			obj.pdf2excel()
			del obj
	elif len(sys.argv) == 2:
		if argument[1] == '--help':
			help()

if __name__ == '__main__':
    main()