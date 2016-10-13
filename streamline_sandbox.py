
import os

input_file = "C:/Users/Schuyler/Documents/Sandbox/ShuttleFile_VentureParks_20160908.TXT"
file_data_buffer = []
sitedata = []
livedata = True


with open(input_file, 'r') as alldata:
	for line in alldata:
		if line.startswith("Calibration:"):
			file_data_buffer = []
		file_data_buffer.append(line)
		if line.startswith("END OF DATA"):
			for outline in file_data_buffer:
				sitedata.append(outline)
	print(sitedata)