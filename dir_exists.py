
import os

#	checks to see if directory exists. 
#	if true then dir not created
#	if false then dir is created
def path_exists(dirs):
	if os.path.isdir(dirs + "/ShuttleOutput/"):
		print("That Directory Already Exists!")
	else:
		os.makedirs(dirs + "/ShuttleOutput/")
		

def main_newfile():
    userPath = input("Enter the New filefolder path:")
    path_exists(userPath)

main_newfile()
