

import os

def csvfile(user_filepath = "Input filepath directory:"):
	while true:
		filepath = input(user_filepath)
	#print(path)
	#print(filename)
		for files in os.walk(filepath):
			for file in files:
				print(file)
			#with open(filepath, 'r') as sitedata:
			#	sitelines = sitedata.readlines()
				
				#creates the filename 
			#	for line in sitelines:
			#		if "*Counter name   :" in line:
			#			sitename = line[19:].strip()
			#			
			#		if "=DOCK TIME" in line:
			#	filename = sitename + "_" + filedate
			#	print(filename)
			#	with open(filepath % "/%s.TXT" % filename, 'w')as siteout:	
			#		siteout.write("sitename, date, time, count\n")
			#
			#		for line in sitelines:
			#		print(sitelines)