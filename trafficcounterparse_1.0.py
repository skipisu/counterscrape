


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

def site_files(shuttledata_output_dir):
	"""		converts text files from the counterscrape script to a csv format								"""
	"""		creates new temp counter data directory "/SiteOutput/" if not present.						"""
	"""		if temp directory ".../SiteOutput" present prompts user to delete or move directory.		""" 
	
	
	# os.path.dirname(user_filepath)	
	sitedata_output_dir = shuttledata_output_dir + "SiteOutput/"
	
	
	if os.path.isdir(sitedata_output_dir):
		print("\n\nThe Directory <<< %s >>> \nAlready Exists!!!" % sitedata_output_dir, \
		"\n\n	<<<   Please Delete or Move Directory and Files!!!   >>>\n"\
		"\n	<<<   Returning Back To Traffic Site File Script Prompt!!!   >>>\n")
		return counterdata_parse()
	else:
		os.makedirs(sitedata_output_dir)
		print("\nDirectory Created!\n",str(datetime.datetime.now().strftime("%H:%M:%S")),\
		"Output file: <<< %s >>>\n\n" % sitedata_output_dir)
		
	for site_file in os.listdir(shuttledata_output_dir):
		sitedata = os.path.join(shuttledata_output_dir, site_file)
		
		if os.path.isfile(sitedata):
		
			with open(sitedata, 'r') as sites:
				sitelines = sites.readlines()

				#	creates the filename 
				for line in sitelines:
					if "*Counter name   :" in line:
						sitename = line[19:].strip()

					if "=DOCK TIME" in line:
						filedate = line[28:].strip().replace("-", "").replace(" ", "_").replace(":", "")
				
				filename = sitename + "_" + filedate
				
				with open(sitedata_output_dir + '%s.TXT' % filename, 'w') as site_out:
					site_out.write("sitename, date, time, count\n")
					
					for line in sitelines:
					
					#	extracts traffic counter name as 'sitename' 
						if "*Counter name   :" in line:
							sitename = line[19:].strip()

						#	combines 'sitename' and 'line' stripped to complete the file if line begins with a number
						if line[0].isdigit():
							alldata = sitename + ',' + line.strip()
							site_out.write(alldata + '\n')					
					print(str(datetime.datetime.now().strftime("%H:%M:%S")),   "   Creating File:   <<<" + sitedata_output_dir + "%s.TXT>>>" % filename)
	input("\n\nPress Enter to Exit!")


	
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
		"\n	<<<   Returning Back to the Parsing Prompt!!!\       >>>\n")
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
	site_files(shuttledata_output_dir)


def counterdata_parse():
	"""   calls for the file for parsing	"""
	""" executes "file_splitter" above 	"""
	
	user_filepath = input("\n\n		WELCOME TO THE TRAFFIC DATA PARSING SCRIPT!\n"\
	"\nTraffic Counter Raw Data File Parsing Script Running...\n"\
	"\nEnter Full Filepath For The Traffic Counter File To Be Parsed:\n")
	rawfile_dirs(user_filepath)

		
counterdata_parse()