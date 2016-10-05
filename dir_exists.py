
import os

def path_exists(dirs):
    if not os.path.isdir(dirs):
        os.makedirs(dirs)

def main_newfile():
    userPath = input("Enter the New filefolder and path:")
    path_exists(userPath)

main_newfile()
