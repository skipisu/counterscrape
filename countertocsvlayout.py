

import os
import datetime


def site_files(user_filepath):
	"""		converts text files from the counterscrape script to a csv format								"""
	"""		creates new temp counter data directory "/SiteOutput/" if not present.						"""
	"""		if temp directory ".../SiteOutput" present prompts user to delete or move directory.		""" 
	
	
	os.path.dirname(user_filepath)	
	sitedata_output_dir = user_filepath + "/SiteOutput/"
	
	
	if os.path.isdir(sitedata_output_dir):
		print("\n\nThe Directory <<< %s >>> \nAlready Exists!!!" % sitedata_output_dir, \
		"\n\n	<<<   Please Delete or Move Directory and Files!!!   >>>\n"\
		"\n	<<<   Returning Back To Traffic Site File Script Prompt!!!   >>>\n")
		return counterdata_sites()
	else:
		os.makedirs(user_filepath + "/SiteOutput/")
		print("\nDirectory Created!\n",str(datetime.datetime.now().strftime("%H:%M:%S")),\
		"Output file: <<< %s >>>\n\n" % sitedata_output_dir)

	sitedata_txt(user_filepath)



def sitedata_txt(user_filepath):
	site_outpath = user_filepath + "/SiteOutput/"	

		
	for site_file in os.listdir(user_filepath):
		sitedata = os.path.join(user_filepath, site_file)
		
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
				
				with open(site_outpath + '%s.TXT' % filename, 'w') as site_out:
					site_out.write("sitename, date, time, count\n")
					
					for line in sitelines:
					
					#	extracts traffic counter name as 'sitename' 
						if "*Counter name   :" in line:
							sitename = line[19:].strip()

						#	combines 'sitename' and 'line' stripped to complete the file if line begins with a number
						if line[0].isdigit():
							alldata = sitename + ',' + line.strip()
							site_out.write(alldata + '\n')					
					print(str(datetime.datetime.now().strftime("%H:%M:%S")),   "   Creating File:   <<<" + site_outpath + "%s.TXT>>>" % filename)

		
def counterdata_sites():
	"""		prompts user for the file path location where files to be converted to csv format "site_files()" """
	
	user_filepath = input("\n\n   		WELCOME TO THE TRAFFIC COUNTER SITE DATA TO CSV LAYOUT SCRIPT!\n"\
		"\nTraffic Counter Site Data Files Script Running...\n"\
		"\nEnter Filepath To The Parsed Traffic Counter Files To Be Processed As CSV Format/Layout:  \n")
	
	site_files(user_filepath)

counterdata_sites()