#############################################################################
#############################################################################
#############################################################################
#																			#
#	created by : Schuyler Sampson											#
#	created with: Python 3.4.4												#
#																			#
#	This script will rename the idividual file listed in the file path		#
#	after splitting. The script copies the name and date of traffice 		#
#	counter was downloaded and use the name and date to rename the file		#
#																			#
#	1.) Replace the file path with the filepath in the first 				#
#		open statement														#
#	2.) Check to make sure the file path is correct in the 	second open 	#
#		statement. This is where the renamed files will go					#
#	3.) Execute the script in Python										#
#																			#
#############################################################################
#############################################################################
#############################################################################

import os

with open("C:/Users/schuyler.sampson/Documents/Sandbox/ShuttleOutput/ShuttleFile_VentureParks_20160908_2.TXT", "r")\
		as sitedata:
		sitelines = sitedata.readlines()
		
		#creates the filename 
		for line in sitelines:
			if "*Counter name   :" in line:
				sitename = line[19:].strip()
				
			if "=DOCK TIME" in line:
				filedate = line[28:].strip().replace("-", "").replace(" ", "_").replace(":", "")
		filename = sitename + "_" + filedate
		with open("C:/Users/schuyler.sampson/Documents/Sandbox/ShuttleOutput/%s.TXT" % filename, 'w')\
		as siteout:	
			siteout.write("sitename, date, time, count\n")
			
			for line in sitelines:
		
				#extracts traffic counter name as 'sitename' 
				if "*Counter name   :" in line:
					sitename = line[19:].strip()

				#combines 'sitename' and 'line' stripped to complete the file if line begins with a number
				if line[0].isdigit():
					alldata = sitename + ',' + line.strip()
					siteout.write(alldata + '\n')