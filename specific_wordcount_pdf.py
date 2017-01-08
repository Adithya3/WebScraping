import PyPDF2

def page_reader(single_page_object,string_to_count):	
	count=0
	page_text=single_page_object.extractText()
	individual_words=page_text.split()
	for word in range(0,len(individual_words)):
		if individual_words[word]==string_to_count:
			count=count+1
		else:
			count=count	
	#print count
	return count


	

pdf_location=raw_input("type the pdf file location = ")
string_to_count=raw_input("enter the word to be counted = ")
pdf_object=PyPDF2.PdfFileReader(open(pdf_location,'rb'))
number_of_repetitions=0

for page in range(1,pdf_object.getNumPages()):
	page_object=pdf_object.getPage(page)
	repetition_in_page=page_reader(page_object,string_to_count)
	number_of_repetitions=number_of_repetitions+repetition_in_page


print 	number_of_repetitions
