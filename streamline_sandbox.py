

#work file:	"C:/Users/schuyler.sampson/Documents/Sandbox/ShuttleFile_VentureParks_20160908.TXT"
#home file:	"C:/Users/Schuyler/Documents/Sandbox/ShuttleFile_VentureParks_20160908.TXT"
import os

input_file = "C:/Users/schuyler.sampson/Documents/Sandbox/ShuttleFile_VentureParks_20160908.TXT"
file_data_buffer = []
sitedata = []
livedata = True


with open(input_file, 'r') as alldata:
	for line in alldata:
		# if "*Counter name   :" in line:
			# sitename = line[19:].strip()
		if line.startswith("Calibration:"):
			file_data_buffer = []
			
		file_data_buffer.append(line.strip())
	file_data_buffer.insert(1,"FUCKTHIS")
	print(file_data_buffer)
		# if line.startswith("END OF DATA"):
			# for outline in file_data_buffer:
				# sitedata.append(outline.strip())
				
# print(sitedata)