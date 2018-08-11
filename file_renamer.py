# This application renames files based on a user input directory, word that needs to be changed, and word that it will be changed to.
# It also has optional capabilities to add a date stamp to a .txt file that has been renamed

import os
import datetime as dt

def file_renamer(path, original, new, datestamp = False):
    '''This accepts a filepath, a string that the user wants changed, and the new string that will be changed to.'''
    '''It also has an optional datestamp functionality that will add an edited on Timestamp for any .txt file that needs renaming'''
    # changes the path that python is looking at
    os.chdir(path)

    # creating flags that will tell us whether or not there were any files or any files that needed renaming
    flag1, flag2 = 0, 0

    # walk through each file in the folder
    for file in os.listdir(path):
        # check if the file is actually a file and not a directory
        if os.path.isfile(file):
            #setting flag1 means there are actual files in directory
            flag1 = 1
            #checking to see if file needs renaming
            if original in file:
                os.rename(file, file.replace(original, new))
                flag2 = 1
                #checking if the datestamp functionality was passed and will only pass to txt files
                if datestamp and (file[-4:] == '.txt'):
                    # opening that ALREADY RENAMED text file and stamping it and then closing it
                    text_file = open(file.replace(original, new), "a") #using 'a' file access mode means it will append to that text file - and not overwrite the old stuff
                    text_file.write("\n\n\n\n\nEdited on " + str(dt.date.today()) + "\n")
                    text_file.close()

    #using the flags to tell the user if there were any errors or not in the process
    if not flag1:
        return 'There are no files in this directory.'
    elif not flag2:
        return 'There were no files that required renaiming based on your parameters.'
    else:
        return 'All files renamed!'


# ----------------------- #
# main
# ----------------------- #

while True:
    #ask user for directory input or if user wants to exit
    path = str(input('What directory would you like your files renamed? (or type EXIT): '))
    if path.upper() == 'EXIT':
        print('Goodbye.')
        break

    #checks if directory is valid, then asks user for text to be changed and text to be changed to
    elif os.path.isdir(path):
        original = input('What text string would you like changed? ')
        new = input('What would you like the text string to be changed to? ')

        #checks if user wants to add a datestamp or not to .txt files
        refer = {'Y':True, 'N':False}
        datestamp = refer.get(input('Would you like a datestamp to be placed on all .txt files? (Y or N): ').upper(), 'N')

        #running the function
        print(file_renamer(path, original, new, datestamp))
        break
    else:
        print('Invalid Path.')

# ----------------------------- #
# Test Code:
# ----------------------------- #
# home = os.getcwd()
# path = os.path.join(home, 'Test Rename')
# original = '(draft)'
# new = '(final)'
# datestamp = True
# print(file_renamer(path, original, new, datestamp))
