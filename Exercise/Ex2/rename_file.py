import os

def rename_file():
    #get file from folder
    file_list = os.listdir(r"/Users/Ken/Desktop/Udacity_Programming_Python/Exercise/Ex2/prank")
    #print file_list
    saved_path = os.getcwd()
    
    os.chdir(r"/Users/Ken/Desktop/Udacity_Programming_Python/Exercise/Ex2/prank")
    
    #rename file
    for file_name in file_list:
        print ("Old name" + file_name)
        print ("New name" + file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)
    
rename_file()
