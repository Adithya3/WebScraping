def getlinks():
	from bs4 import BeautifulSoup
	import requests
	import os

	#taking the url and the location to where text file should be created
	url=raw_input('enter the url') #enter the url 
	#file_location=raw_input('enter the file location') /// use these if you want to specify the location of the filed
	#file_location=file_location+"/imageurl.txt"
	#print file_location

	#using requests and beautifulsoup to extract content
	r=requests.get(url)
	soup=BeautifulSoup(r.content,"lxml")
	#os.chdir(file_location)
	file_object=open("linksurl.txt","w")

	for link in soup.find_all('a'):
		s1=str(link.text).decode('ascii','ignore')
		file_object.write(link.text)
		s2=str(link.get('href')).decode('ascii','ignore')		
		file_object.write(s2)




getlinks()
