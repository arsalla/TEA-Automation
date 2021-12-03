# ************************READ ME************************
#                 Version 1.1 11/04/2021
# This only runs in VSCode currently, not in exe format
# Only I can run this as of now, so this is not sharable
# These issues will be corrected in future updates. 

import os
from dir_names import *
import datetime

main_dir = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov ,dec]			# Loading the list of sub-directories
year = input("Year: ")
root_dir = 'W:/Risk Control/public/TEA/' + str(year)
main_dir_names = ['01', '02', '03','04', '05', '06', '07', '08', '09', '10', '11', '12'] # Name of the sub-directories

def leapyear(year):
    if int(year) % 4 == 0:
        if int(year) % 100 == 0:
            if int(year) % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0
                
def TEAdirectory():
    # Create directory
    
    for i in range(0, len(main_dir)):
        for j in range(0,len(main_dir[i])):
            daypathval = main_dir[i][j]

            if len(str(daypathval)) == 1:
                daypathval = '0' + str(daypathval)
            dirName = str(root_dir) + '/' + str(main_dir_names[i]) + '/' + str(main_dir_names[i]) + str(daypathval) + str(year)
        
            try:
                # Create target Directory
                os.makedirs(dirName)
                print("Directory " , dirName ,  " Created ") 
            except FileExistsError:
                print("Directory " , dirName ,  " already exists")        
            
            # Create target Directory if don't exist
            if not os.path.exists(dirName):
                os.makedirs(dirName)
                print("Directory " , dirName ,  " Created ")
            else:    
                print("Directory " , dirName ,  " already exists")

    leapyearbo = leapyear(year)
    if leapyearbo == 1:
                print ('Leap Year: TRUE')
                dirName = 'W:/Risk Control/public/TEA/' + str(year) + '/02/0229' + str(year)
                if not os.path.exists(dirName):
                    os.makedirs(dirName)
                    print("Directory " , dirName ,  " Created ")
                else:    
                    print("Directory " , dirName ,  " already exists")
    else:
        print('Leap Year: FALSE')
    print('Process Complete.\n\nThere is a "45th" day added into every month\nYou must delete this manually\nThis will be fixed in version 1.2')
        
    # Code to remove extra '45' files created, 
    # for i in range (0, len(main_dir_names)):
    #    os.remove(str(root_dir) + '/' + str(main_dir_names[i]) + '/' + str(main_dir_names[i]) + '45' + str(year))

def FileParse():
    directory = 'W:/Risk Control/public'
    templist = [10000]
    for filename in os.listdir(directory):
        num = 0
        if filename.endswith('.xlsx'):
            templist [num] = filename
            num =+ 1
    print (templist)


def main():
    search = input('Select what to create:\n1)  TEA Daily Folders\n2)   Public Monthly\n')
    if search == "1":
        TEAdirectory()
    elif search == "2":
        FileParse()
    else:
        print('Invalid Selection')

if __name__ == "__main__":
    main()


