import os #import os module to deals with dirs
import shutil #import shutil module to deals with high level file operations

def file_organizer(path):
    #shutil.disk_usage() is used to show the disk usage in bytes
    shutil.disk_usage(path)[1]/(1024*1024*1024)
    #list all the file in the dirs
    list_of_file=os.listdir(path)
    #Use for loop to iterate over the files in the folder
    for item in list_of_file:
        name,extension=os.path.splitext(item)
        print(name,extension)
        extension=extension[1:]
        if os.path.exists(path+'/'+extension):
            shutil.move(path+'/'+item, path+'/'+extension+'/'+item)
        else:
            #It makes the dirs to store
            os.makedirs(path+'/'+extension)
            shutil.move(path+'/'+item, path+'/'+extension+'/'+item)
#main_function

path=r'D:\p' #USE YOUR OWN PATH TO ORGANIZE THE FILE HERE
file_organizer(path)

            
            
    
    
    
