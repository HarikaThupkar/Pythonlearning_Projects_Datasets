#!/usr/bin/env python
# coding: utf-8

# # How to copy files from one folder to another folder using Python?
# 

# In[9]:


import shutil, os
files = ['C://Users//pavan//git_projects//Pythonlearning_Projects_Datasets//Python_Forloops_comprehension_list.txt','C://Users//pavan//git_projects//Pythonlearning_Projects_Datasets//Python_topics_to_work.txt']
for f in files:
    shutil.copy(f,'C://Users//pavan//git_projects//New_Test_Folder')


# # Using Python pathlibPath.exists() For Python 3.4
# 

# In[10]:


import pathlib
file = pathlib.Path("C://Users//pavan//git_projects//New_Test_Folder")
if file.exists ():
    print ("File exist")
else:
    print ("File not exist")


# # Using Python os.path.exists()
# 

# In[11]:


import os.path
from os import path

def main():

   print ("File exists:"+str(path.exists('C://Users//pavan//git_projects//New_Test_Folder')))
   

if __name__== "__main__":
   main()


# # Using Python os.path.isfile()
# 

# In[14]:


import os.path
from os import path

def main():

	print ("Is it File?" + str(path.isfile('C://Users//pavan//git_projects//New_Test_Folder')))

if __name__== "__main__":
	main()


# # Using Python os.path.isdir()

# In[15]:



import os.path
from os import path

def main():

   print ("Is it Directory?" + str(path.isdir('C://Users//pavan//git_projects//New_Test_Folder')))
  
if __name__== "__main__":
   main()


# # Complete Code
# 
# 

# In[16]:


import os
from os import path

def main():
    # Print the name of the OS
    print(os.name)
#Check for item existence and type
print("Item exists:" + str(path.exists("C://Users//pavan//git_projects//New_Test_Folder")))
print("Item is a file: " + str(path.isfile("C://Users//pavan//git_projects//New_Test_Folder")))
print("Item is a directory: " + str(path.isdir("C://Users//pavan//git_projects//New_Test_Folder")))

if __name__ == "__main__":
    main()


# # How to check If File Exists
# 

# In[ ]:


os.path.exists() – Returns True if path or directory does exists.
os.path.isfile() – Returns True if path is File.
os.path.isdir() - Returns True if path is Directory.
pathlib.Path.exists() - Returns True if path or directory does exists. (In Python 3.4 and above versions)

