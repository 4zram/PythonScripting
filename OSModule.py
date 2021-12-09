"""
Os Module is used to interact with the operating system. We can create, delete, move folders using this.
While typing paths, note that only double backslash or single front slash will work.
"""
import os

# print(os.getcwd()) # Will print the current working directory
# os.chdir("D:/") # Will change the current directory to the defined path.
# print(os.getcwd())
# print(os.listdir()) # Will list all the elements under the path.
# os.mkdir("D:\\SomeFolder\\Find") # Will create a folder
# os.rmdir("D:/SomeFolder/Find") # Will delete the folder
# os.remove("D:/SomeFolder/snap.txt") # Will remove the file from the folder

# os.path is another handy sub-module

# print(os.path.join("D:\\SomeFolder","D:\\SomeFolder\\otherfile.txt")) # Will join the two paths
# print(os.path.split("D:\\SomeFolder\\thisfolder\\otherfile.txt")) # Will split the two paths
# print(os.path.exists("D:\\SomeFolder\\thisfolder\\otherfile.txt")) # Will check if the given path exists or not.