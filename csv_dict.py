import os
import pprint
DATADIR = "/home/adithya/Downloads"
DATAFILE = "beatles-diskography.csv"

def parse_file(datafile):
	data=[]
	with open(datafile,"r") as f:
		for line in f:
			data.append(line)
	new_data=[]
#	return data
	keys=data[0].split(",")
	for i in range(10):
		new_dict={}
		new_list=data[i+1].split(",")
		for j in range(len(new_list)):
			new_dict[keys[j]]=new_list[j]
		new_data.append(new_dict)
	return new_data
			
	



if __name__=="__main__":
	datafile=os.path.join(DATADIR,DATAFILE)
	d=parse_file(datafile)
	firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
	tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
	#assert d[0]==firstline
	#assert d[9]==tenthline
	pprint.pprint(d)
	
