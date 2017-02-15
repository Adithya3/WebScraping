import os
import xmltodict
import json


def csv_json(DATAFILE_LOCATION1,DATAFILE_LOCATION2):
	sd= open(DATAFILE_LOCATION1,'rb')
	r=sd.read()
	jdata=xmltodict.parse(r)
	sd.close()

	bb=open(DATAFILE_LOCATION2,"wb")
	jjdata=json.dumps(jdata)
	bb.write(jjdata)
	bb.close()



if __name__=="__main__":
	DATAFILE_LOCATION1=raw_input("Enter the xml file location")
	#pprint.pprint(data)
	DATAFILE_LOCATION2=raw_input("enter the file where json will be stored")
	csv_json(DATAFILE_LOCATION1,DATAFILE_LOCATION2)
