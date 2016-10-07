

import os

rawcounterfile = "C:/Users/schuyler.sampson/Documents/Sandbox/ShuttleFile_VentureParks_20160908.TXT"

path, filename = os.path.split(rawcounterfile)
basename, ext = os.path.splitext(filename)
	
with open(rawcounterfile, 'r')\
    as rawdata:
		rawdata_lines = rawdata.readlines()	#creates list called datalines
		i = 1               # establishes starting point for naming new files 1 to n
		for line in rawdata_lines:
			if line.strip():
				rawdata_lines.append(line)
				
			if line.strip() == "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<":
				#creates the filename by site
				for line in rawdata_lines:
					if "*Counter name   :" in line:
						sitename = line[19:].strip()
					if "=DOCK TIME" in line:
						filedate = line[28:].strip().replace("-", "").\
						replace(" ", "_").replace(":", "")
				filename = sitename + "_" + filedate
				with open("C:/Users/schuyler.sampson/Documents/Sandbox/ShuttleOutput/%s.TXT" % filename, 'w')\
				as siteout:	
					siteout.write("sitename, date, time, count\n")
					for line in rawdata_lines:
		
						#extracts traffic counter name as 'sitename' 
						if "*Counter name   :" in line:
							sitename = line[19:].strip()
						
						#combines 'sitename' and 'line' stripped to complete the file if line begins with a number
						if line[0].isdigit():
							alldata = sitename + ',' + line.strip()
							siteout.write(alldata + '\n')
        #   f_output = os.path.join(path, '{}_{}{}'.format(basename, i, ext))
	    #	f_out = open(f_output, 'w')
        #    f_out.write(''.join(datalines))
        #    f_out.close()
        #    i += 1
        #    datalines = []
