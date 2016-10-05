

#############################################################################
#############################################################################
#									    #
#	created by : Schuyler Sampson                                       #
#	created with: Python 3.4.4					    #
#									    #
#	This file is used for splitting the traffic counter files           #
#	It will split the master counter file from teh TRAFX Counters       #
#	                                                                    #
#									    #
#	1.) Copy and Paste Raw Coutner File into a "sanbox" folder	    #
#	2.) Exectute this file in Python (crtl+F1)			    #
#	3.) Copy and past the complete filepath of the file to parsed       #
#           when the prompt appears. (you do not need to include open       #
#           and close quoatation marks for the filepath)                    #
#	4.) This program will split/parse the data file into individual     #
#           text files by site. each file will be renamed as the original   #
#           but with the a "_n".txt                                         #
#	    file directory of the raw file  			            #
#	5.) Close the Python console window when completed		    #
#									    #
#############################################################################
#############################################################################


import os


def file_splitter(fullfilepath):
	#   splits text file based on a splitting identifier
	path, filename = os.path.split(fullfilepath)
	basename, ext = os.path.splitext(filename)

	#   opens the original source text file
	with open(fullfilepath, 'r') as rawdata:
		datalines = []	#creates list called "datalines"
		i = 1 
		
		# reads each line data from "rawdata"
		for line in rawdata:
			if line.strip():
				datalines.append(line)
			if line.strip() == "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<":
				f_output = os.path.join(path, '{}_{}{}'.format(basename, i, ext))
				f_out = open(f_output, 'w')
				f_out.write(''.join(datalines))
				f_out.close()
				i += 1
				datalines = []

#   calls for the file for parsing and executes "file_splitter" above
def counterdata_parse():
	user_filepath = input("Enter filepath to the Traffic Counter File to be Parsed:  ")
	file_splitter(user_filepath)

counterdata_parse()
