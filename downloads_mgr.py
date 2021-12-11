#Program to manage files in downloads folder.
import os
import shutil
from os.path import isfile, join
from os import listdir, path


def folder_scan(my_path):

    """
    Function to scan your download folder and give a summary
    """
    y = 0
    n = 0
    for i in listdir(my_path):
        if isfile(join(my_path, i)):
            y = y+1
        else:
            n = n+1
    print("After scanning your downloads total " + str(y) + " files found and " + str(n) + " docs not classified as files" )


def sort_files(my_path):
    """
    Function to scan the folder, sort files and add file names to a dictionary
    """
    file_types = []
    file_types_folder_dict={}
    files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
    
    #Loop to loop through the files, create folders for files
    for file in files:
        file_name_rev = file[::-1]
        file_type = file_name_rev.split(".")[0][::-1]
        file_types.append(file_type)
        new_folder_name = my_path + "/" + file_type + "_folder"
        file_types_folder_dict[str(file_type)] = str(new_folder_name)
        if os.path.isdir(new_folder_name) == True:
            continue
        else:
            os.mkdir(new_folder_name)   
    
    #Loop tp move the files to respective folder based in the type
    for file in files:

        """
        Function to move the files into their respective folder
        """

        current_path = my_path + "/" + file
        file_name_rev = file[::-1]
        file_type = file_name_rev.split(".")[0][::-1]
        if file_type in file_types_folder_dict.keys():
            dest_path = file_types_folder_dict[str(file_type)]
            shutil.move(current_path, dest_path)

    
if __name__ == "__main__":
    my_path = "/Users/akhilzeeb/Downloads"
    folder_scan(my_path)
    sort_files(my_path)