

import os
import datetime 

#work location:	C:/Users/schuyler.sampson/Documents/Sandbox/ShuttleOutput
#work location:	C:/Users/schuyler.sampson/Documents/Sandbox/ShuttleOutput/SiteOutput
#home location:	C:/Users/Schuyler/Documents/Sandbox/TestScrape/ShuttleOutput

def sitedata_txt():
	#user_sitefilepath = input("\nSite Data File File Please:\n\n")
	user_filepath = input("\nSite Data File File Please:\n\n")
	site_outpath = user_filepath + "/SiteOutput/"		
	#site_file = []

		
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
sitedata_txt()
			
	
					
	
			
						# # # print("Creating<<<" + site_filepath + "%s.TXT>>>" % filename,\
					# # # # " At " str(datetime.datetime.now().strftime("%H:%M")))