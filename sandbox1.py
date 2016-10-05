

import os

def csvfile(filepath):
	path, filename = os.path.split(filepath)
	#print(path)
	#print(filename)
	for files in os.walk(path):
		for file in files:
			with open(filepath, 'r') as sitedata:
				sitelines = sitedata.readlines()
			#creates the filename 
				for line in sitelines:
					if "*Counter name   :" in line:
						sitename = line[19:].strip()
						
					if "=DOCK TIME" in line:
						filedate = line[28:].strip().replace("-", "").replace(" ", "_").replace(":", "")
				filename = sitename + "_" + filedate
				with open(filepath"/%s.TXT" % filename, 'w')\
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