
import os

#	checks to see if directory exists. 
#	if true then dir not created
#	if false then dir is created
def path_exists(dirs):
	if os.path.isdir(dirs + "/ShuttleOutput/"):
		print("That Directory Already Exists!")
	else:
		os.makedirs(dirs + "/ShuttleOutput/")
		print("ShuttleOutput/ Directory Created!!!")

def new_shuttleoutput():
    userPath = input("Enter the New filefolder path:")
    path_exists(userPath)

new_shuttleoutput()
