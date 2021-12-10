import os
from dir_names import *

main_dir = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov ,dec]			# Loading the list of sub-directories
year = input("Year: ")
main_dir_names = ['01', '02', '03','04', '05', '06', '07', '08', '09', '10', '11', '12'] # Name of the sub-directories

# check if leap year, returns 1 if true, 0 if false
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

# create daily folders for /TEA            
def tea_folders():
    root_dir = 'W:/Risk Control/public/TEA/' + str(year)
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
    print (leapyearbo)
    if leapyearbo == 1:
         leapyrpath = 'W:/Risk Control/public/TEA/' + str(year) + '/02/0229' + str(year)
         if not os.path.exists(leapyrpath)
            os.makedirs(leapyrpath)
            print ('Directory ' + leapyrpath + ' Created')
    # Remove excess '45' date folders
    for i in range (0, len(main_dir_names)):
        os.rmdir(str(root_dir) + '/' + str(main_dir_names[i]) + '/' + str(main_dir_names[i]) + '45' + str(year))

folder_tree_results = []

# search public folder for individual folders that need yearly folders
def folder_tree_search():
    for roots, dirs, files in os.walk("W:\Risk Control\public"):
        for dir in dirs:
            # if there is pre-existing year folders, add path to list
            if dir == '2021':
                folder_tree_results.append(roots)

def misc_folders():

    folder_tree_search()
    # for every necessary folder
    for element in folder_tree_results:
        # for every month
        for month in main_dir_names:
            # create folder in dir for each month
            dir_name = element + '\\' + year + '\\' + month
            os.makedirs(dir_name)
            # confirmation
            print ('Directory ' + dir_name + ' has been created')
        
def main():
    tea_folders()
    misc_folders()


if __name__ == '__main__':
    main()



