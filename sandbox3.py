


import os

#Home FilePath: C:/Users/Schuyler/Documents/Sandbox/TestScrape/ShuttleFile_VentureParks_20160908.TXT

def file_splitter(fullfilepath):
	"""		check if ShuttleOuput/ directory exists			"""
	"""		creates /ShuttleOutput/ directory if not exists	"""
	"""		splits text file based on a splitting identifier	"""
	
	path, filename = os.path.split(fullfilepath)
	basename, ext = os.path.splitext(filename)
	shuttle_output_dir = path + "/ShuttleOutput/"
	
	if os.path.isdir(shuttle_output_dir):
		print("\n\nThat Directory Already Exists!")
	else:
		os.makedirs(shuttle_output_dir)
		print("\n\nDirectory <<<%s>>> Created!!!" % shuttle_output_dir)
	
	
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
				f_output = os.path.join(shuttle_output_dir, '{}_{}{}'.format(basename, i, ext))
				f_out = open(f_output, 'w')
				f_out.write(''.join(rawdata_lines))
				f_out.close()
				i += 1
				rawdata_lines = []


def counterdata_parse():
	"""   calls for the file for parsing	"""
	""" executes "file_splitter" above 	"""
	
	user_filepath = input("\nEnter Full Filepath For The Traffic Counter File To Be Parsed:\n")
	file_splitter(user_filepath)
	
		
counterdata_parse()