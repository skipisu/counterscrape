

import os

fullfilepath = "C:/Users/schuyler.sampson/Documents/Sandbox/ShuttleFile_VentureParks_20160908.TXT"

path, filename = os.path.split(fullfilepath)
basename, ext = os.path.splitext(filename)
	
with open(fullfilpath, 'r')\
    as rawdata:
    datalines = []	#creates list called datalines
    i = 1               # establishes starting point for iteration
    for line in rawdata:
        if line.strip():
            test = datalines.append(line)
        if line.strip() == "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<":
            f_output = os.path.join(path, '{}_{}{}'.format(basename, i, ext))
	    f_out = open(f_output, 'w')
            f_out.write(''.join(datalines))
            f_out.close()
            i += 1
            datalines = []
