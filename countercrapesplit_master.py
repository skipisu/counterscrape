#############################################################################
#############################################################################
#############################################################################
#																			#
#	created by : Schuyler Sampson											#
#	created with: Python 3.4.4												#
#																			#
#		This file is used for splitting the traffic counter files			#
#		It will split the master counter file requeseted when 				#
#	file_splitter() is entered at the python prompt.  						#
#																			#
#	1.) Copy and Paste Raw Coutner File into a "sanbox" folder				#
#	2.) Exectute this file in Python (crtl+F1)								#
#	3.)	Type file_splitter("file_path_of_Raw_File") and hit enter.	 		#
#	4.) Split Files will be placed in the same								#
#		file directory of the raw file										#
#	5.) Close the Python console window										#
#																			#
#############################################################################
#############################################################################
#############################################################################

import os

def file_splitter(fullfilepath):
	"""splits text file based on a splitting identifier"""
	path, filename = os.path.split(fullfilepath)
	basename, ext = os.path.splitext(filename)

	#	opens the original source text file
	with open(fullfilepath, 'r') as rawdata:
		datalines = []	#creates list called datalines
		i = 1 
		for line in rawdata:
			if line.strip():
				datalines.append(line)
			if line.strip() == "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<<<<":
				f_output = os.path.join(path, '{}_{}{}'.format(basename, i, ext))
				f_out = open(f_output, 'w')
				f_out.write(''.join(datalines))
				f_out.close()
				i += 1
				datalines =[]