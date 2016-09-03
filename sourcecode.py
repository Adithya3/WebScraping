#can get the sourcecode of the website

from bs4 import BeautifulSoup
import requests
import os


#taking the url and the location to where text file should be created
url=raw_input('enter the url') #enter the url 

#using requests and beautifulsoup to extract content
r=requests.get(url)
soup=BeautifulSoup(r.content,"lxml")
file_object=open("imageurl.txt","w")
#writing the webcontent into a file
web_content=str(soup)
file_object.write(web_content)

