


import os



def file_splitter(fullfilepath):
	#   splits text file based on a splitting identifier
	path, filename = os.path.split(fullfilepath)
	basename, ext = os.path.splitext(filename)
	shuttle_output_dir = path + "/ShuttleOutput/"
	
	if os.path.isdir(shuttle_output_dir):
		print("That Directory Already Exists!")
	else:
		os.makedirs(shuttle_output_dir)
		print("/ShuttleOutput/ Directory Created!!!")
	
	
	#   opens the original source text file
	with open(fullfilepath, 'r') as rawdata:
		datalines = []	#creates list called "datalines"
		i = 1 
		
		# reads each line data from "rawdata"
		for line in rawdata:
			if line.strip():
				datalines.append(line)
			if line.strip() == "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<":
				f_output = os.path.join(shuttle_output_dir, '{}_{}{}'.format(basename, i, ext))
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