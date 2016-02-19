import os, zipfile

dir_name = '/home/dano8957/panda/GDELT'
extension = ".zip"

os.chdir(dir_name) # change directory from working dir to dir with files

for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for chosen extension
        file_name = os.path.abspath(item) # get absolute path (real path)
        zip_ref = zipfile.ZipFile(file_name) # create zipfile object instance
        zip_ref.extractall(dir_name) # extract all files in that folder
        zip_ref.close() # close zip file
        os.remove(file_name) # delete old zipped files
