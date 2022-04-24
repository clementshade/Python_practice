import os


dir_1 = "nonsense"

parent_dir = "C:/Users/CLEMENT OBIEKE/Desktop/"

path = os.path.join(parent_dir,dir_1)

exist = os.path.exists(path)
if exist == True:
    print('Folder already exist')
else:
    os.makedirs(path)
    print("Folder created sucessfully")
file_name = "myfile.txt"
f = open(os.path.join(path,file_name),"w")
f.write("""Why, HEllo There.""")

f.close()

print("Directory %s created"% dir_1) 
