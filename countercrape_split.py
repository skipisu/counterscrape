


#
#		created by : Schuyler Sampson
#		created with: Python 3.4.4
#
#	This file is used for splitting the TRAFX traffic counter files
#	It will split the master counter file from teh TRAFX Counters
#
#
#


import os
import datetime


def rawfile_dirs(fullfilepath):
	"""		check if ShuttleOuput/ directory exists			"""
	"""		creates /ShuttleOutput/ directory if not exists	"""
	"""		splits text file based on a splitting identifier	"""
	
	path, filename = os.path.split(fullfilepath)
	basename, ext = os.path.splitext(filename)
	shuttledata_output_dir = path + "/ShuttleOutput/"
	
	if os.path.isdir(shuttledata_output_dir):
		print("\n\nThe Directory <<< %s >>> \nAlready Exists!!!" % shuttledata_output_dir, \
		"\n\n	<<<   Please Delete or Move Directory and Files!!!   >>>\n"\
		"\n	<<<   Returning Back to the Parsing Prompt!!!\   >>>n")
		return counterdata_parse()
	else:
		os.makedirs(shuttledata_output_dir)
		print("\n",str(datetime.datetime.now().strftime("%H:%M")), "Directory <<< %s >>> Created!\n" % shuttledata_output_dir)
	
	#   opens the original source text file
	with open(fullfilepath, 'r') as rawdata:
		rawdata_lines = []
		i = 1 
		
		#	reads each line data from "rawdata" splits file by identifier line
		#	creates all txt files represented in teh raw file 
		for line in rawdata:
			if line.strip():
				rawdata_lines.append(line)
			if line.strip() == "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<":
				f_output = os.path.join(shuttledata_output_dir, '{}_{}{}'.format(basename, i, ext))
				f_out = open(f_output, 'w')
				f_out.write(''.join(rawdata_lines))
				f_out.close()
				i += 1
				rawdata_lines = []
				print(str(datetime.datetime.now().strftime("%H:%M")),	"   Creating   <<< %s >>>" % f_output)

def counterdata_parse():
	"""   calls for the file for parsing	"""
	""" executes "file_splitter" above 	"""
	
	user_filepath = input("\n\n		WELCOME TO THE TRAFFIC DATA PARSING SCRIPT!\n"\
	"\nTraffic Counter Raw Data File Parsing Script Running...\n"\
	"\nEnter Full Filepath For The Traffic Counter File To Be Parsed:\n")
	rawfile_dirs(user_filepath)
	
		
counterdata_parse()