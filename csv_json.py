import os
import pprint
import csv


def csv_json(DATAFILE_LOCATION1,DATAFILE_LOCATION2):
	data=[]
	n=0
	with open(DATAFILE_LOCATION1,'rb') as sd:
		r=csv.DictReader(sd)
		for i in r:
			data.append(i)
	with open(DATAFILE_LOCATION2,"WB") as bb:
		bb.write(data)




if __name__=="__main__":
	DATAFILE_LOCATION1=raw_input("Enter the csv file location")
	#pprint.pprint(data)
	DATAFILE_LOCATION2=raw_input("enter the file where json will be stored")
	csv_json(DATAFILE_LOCATION1,DATAFILE_LOCATION2)
