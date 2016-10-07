import os
import csv


rawcounterfile = "C:/Users/schuyler.sampson/Documents/Sandbox/ShuttleFile_VentureParks_20160908.TXT"

filepath, filename = os.path.split(rawcounterfile)
basename, ext = os.path.splitext(filename)

rawdata_lines = []
sitedata_lines = []
i = 1	

#def read_file(rawcounterfile):
with open(rawcounterfile, 'r') as rawdata:
	next(rawdata)
	for line in rawdata:
		if line.strip():						#skip empty lines
			rawdata_lines.append(line)	#creates list called datalines
				
		if line.strip() == "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<":
			for line in rawdata_lines:
				if "*Counter name   :" in line:
					sitename = line[19:].strip()
					
				if "=DOCK TIME" in line:
					filedate = "20" + line[28:-9].strip().replace("-", "")
			site_filename = sitename + "_" + filedate
	
			#f_output = os.path.join(filepath, '{}_{}{}'.format(site_filename, i, ext))
			#sitedata_lines = open(f_output, 'w')
			sitedata_lines  = write(''.join(rawdata_lines))
			#f_out.close()
			sitedata_lines = []

		
		
		
		
		
		
		
		#	reads and sppends data from file line by line
		#for line in rawdata_lines:
		#	if line.strip():
		#		rawdata_lines.append(line)
		#		print(rawdata)