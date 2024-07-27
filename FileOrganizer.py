import os
import shutil
import time


def organizefiles(path):
    files = os.listdir(path)   # Storing all files from the path

    # Splitting files and getting file type
    for file in files:
        filename,extension = os.path.splitext(file)    # function to split filename and type
        extension = extension[1:]  # save file type in extension without dot '.'

        if os.path.exists(path + '/' + extension.upper()):  # Checking if thw folder is already existed in Path
            # Moving relevant files into the folder
            shutil.move(path + '/' + file, path + '/' + extension.upper() + '/' + file)
        else:
            # Creating folder having File type name.
            os.makedirs(path + '/' + extension.upper())
            # Moving relevant files into the folder
            shutil.move(path + '/' + file, path + '/' + extension.upper() + '/' + file)
            print(f' The {file} is moved successfully to {extension.upper()} folder')


if __name__ == '__main__':
    Path_to_Organize = input('Enter path')  # specifying the Path to organize
    while True:
        organizefiles(Path_to_Organize)
        time.sleep(30)