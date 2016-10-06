

import os

rawcounterfile = "C:/Users/schuyler.sampson/Documents/Sandbox/ShuttleFile_VentureParks_20160908.TXT"

path, filename = os.path.split(rawcounterfile)
basename, ext = os.path.splitext(filename)
	
with open(rawcounterfile, 'r')\
    as rawdata:
    rawdata_lines = rawdata.readlines()	#creates list called datalines
	#i = 1               # establishes starting point for naming new files 1 to n
    #for line in rawdata_lines:
    #    if line.strip():
    #        test = rawdata_lines.append(line)
	#		print(test)
        #if line.strip() == "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<":
        #    f_output = os.path.join(path, '{}_{}{}'.format(basename, i, ext))
	    #	f_out = open(f_output, 'w')
        #    f_out.write(''.join(datalines))
        #    f_out.close()
        #    i += 1
        #    datalines = []
