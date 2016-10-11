


import os
import datetime
import glob


#C:/Users/schuyler.sampson/Documents/Sandbox/ShuttleOutput/



	user_sitefilepath = input("\nSite Data File File Please:\n\n")
	site_filepath = user_sitefilepath + "SiteOutput/"
	site_file = []
	
	for path, dirs, filename in os.walk(user_sitefilepath):
		for name in filename:
			with open(os.path.join(path, name)) as sites:
				site_file = sites.readlines()
				
				# # #	creates the filename 
				for line in site_file:
					if "*Counter name   :" in line:
						sitename = line[19:].strip()

					if "=DOCK TIME" in line:
						filedate = line[28:].strip().replace("-", "").replace(" ", "_").replace(":", "")
				
				filename = sitename + "_" + filedate
						
		
				with open(site_filepath + "%s.TXT" % filename, 'w') as siteout:	
					siteout.write("sitename, date, time, count\n")
				
					for line in site_file:
										
						#	extracts traffic counter name as 'sitename' 
						if "*Counter name   :" in line:
							sitename = line[19:].strip()

						# 	combines 'sitename' and 'line' stripped to complete the file if line begins with a number
						if line[0].isdigit():
							alldata = sitename + ',' + line.strip()
							siteout.write(alldata + '\n')
							# # # print("Creating<<<" + site_filepath + "%s.TXT>>>" % filename,\
						# # # # " At " str(datetime.datetime.now().strftime("%H:%M")))

