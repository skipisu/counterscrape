

import os
import csv


rawcounterfile = "C:/Users/Schuyler/Documents/Sandbox/ShuttleFile_VentureParks_20160908.TXT"

filepath, filename = os.path.split(rawcounterfile)
basename, ext = os.path.splitext(filename)

rawdata_lines = []
sitedata_lines = []
sitedata = {}
i = 1	


#def path_exists(filepath):
#	if os.path.isdir(filepath + "/ShuttleOutput/"):
#		print("That Directory Already Exists!")
#	else:
#		os.makedirs(filepath + "/ShuttleOutput/")

#def read_file(rawcounterfile):
with open(rawcounterfile, 'r') as rawdata:
	rawdata_lines = rawdata.readlines()
			
	for line in rawdata_lines:
		 if line.strip():
			rawdata_lines.append(line)
	print(rawdata_lines)
		# if line.strip() == "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<":		
			# ''.join(rawdata_lines)
			# i += 1 
			# sitedata_lines = []
	
		# sitedata_lines.append(line)
			# i += 1
			# sitedata_lines = []
	# print(sitedata_lines)
	
#	sitedata_lines = ''.join.rawdata_lines
#	print(sitedata_lines) 
		#skip empty lines
		#	rawdata_lines.append(line)	#creates list called datalines
			
			#sitedata_lines = rawdata_lines.write()
		#print(sitedata_lines)
		# if line.strip() == "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<":
			# for line in rawdata_lines:
				# if "*Counter name   :" in line:
					# sitename = line[19:].strip()
					
				# if "=DOCK TIME" in line:
					# filedate = "20" + line[28:-9].strip().replace("-", "")
			# site_filename = sitename + "_" + filedate
				
			#rawdata_lines.write("sitename, date, time, count\n")
		
				#extracts traffic counter name as 'sitename'  --- from counter to csv
			#if "*Counter name   :" in line:
			#	sitename = line[19:].strip()

			#combines 'sitename' and 'line' stripped to complete the file if line begins with a number
			#if line[0].isdigit():
			#	sitedata = sitename + ',' + line.strip()
			#	siteout.write(sitedata + '\n')
			#sitefile_output = os.path.join(filepath + '/ShuttleOutput/', '{}_{}{}'.format(site_filename, i, ext))
			#sitedata_out = open(sitefile_output, 'w')
			#sitedata_out.write(''.join(rawdata_lines))
			#sitedata_out.close()
			#i += 1
			#sitedata_lines = []


		

#def main_newfile():
#   userPath = input("Enter the New filefolder path:")
#   path_exists(userPath)	