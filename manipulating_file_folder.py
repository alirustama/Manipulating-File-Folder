# -*- coding: utf-8 -*-
"""manipulating_file/folder.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KEgVwmUFApf7UkMrAVG3ways6lxKCOJW
"""

#create a file
"""
steps->
	#open a file

	#give name+extension
	#click enter """

fo=open("/home/spyrustam/Desktop\\exm.txt",'w')
fo.write("Hello!!!")

#to write multiple lines
# create a list of item.
line_list=["How are you? \n","How is the weather there? \n"]
fo.writelines(line_list)

#update a file
"""
steps->
	To update a file, we use same steps
	but open the file in appned mode. """

fo=open("/home/spyrustam/Desktop\\exm.txt",'a')
fo.write("Hello all. Welcome to ISB.")

#to update with multiple lines
# create a list of item.
line_list=["It is really hot in Kolkata.\n","BTW how is your preparation for ISB going on\n","Are you attending the warm up session?\n"]
fo.writelines(line_list)
D:
# use case1
# one file has data for starting 15 days of a month
# other file has data for next 15 days of a month
# you want to update the data in the older file.

#open the first file in append mode
ff=open("/home/spyrustam/Desktop\\example.txt",'a')

#open the second file in read mode
sf=open("/home/spyrustam/Desktop\\exm.txt",'r')
#read data from second file
info=sf.read()/content/D:\Mani\/content/D:\Mani\
##append the info data in the first file
ff.write(info)
#close both the files
ff.close()
sf.close()

# moving a file
#steps->D:
	# change the location of a file.

#importing useful libray
import os
import shutil
# new directory formation-> os.mkdir("new_directiry_path")
os.mkdir("/home/spyrustam/Desktop//ManiPulating FIle")
shutil.move("/home/spyrustam/Desktop//Project _1","/home/spyrustam/Desktop/")



#to copy a file or folder
shutil.copy("/home/spyrustam/Desktop\\4th Semester Result.pdf","/content//home/spyrustam/Desktop\4th Semester Result.pdf")

# to copy multiple files.
#steps
	# for every file , copy it.

file_list=["/home/spyrustam/Desktop\\4th Semester Result.pdf","/home/spyrustam/Desktop\\5th Semester Result.pdf","/home/spyrustam/Desktop\\6th Semester Result.pdf"]
for file in file_list:
	shutil.copy(file,"/home/spyrustam/Desktop/Ptoject_1")

# to rename a file
#steps-> 
	# change the location from old to new

os.rename("/home/spyrustam/Desktop\\1st Sem_res.jpeg","/home/spyrustam/Desktop\\1st Semester Result.jpeg")


# use case 2
# for 2nd Sem_res.jpeg and 3rd Sem_res.jpeg rename it to 2nd Semester Result.jpeg & 3rd Semester Result.jpeg
# we need to make
	# Sem_res.jpeg->  Semester Result.jpeg
# that means we need to makeD:\\Mani\\
	# D:\\2nd Sem_res.jpeg->D:\\2nd Semester Result.jpeg

#creating a list of the files
re_files=["/home/spyrustam/Desktop\\2nd Sem_res.jpeg","/home/spyrustam/Desktop\\3rd Sem_res.jpeg"]
for i in re_files:
	j=i.split(" ")#splitting across a space
	new_path=j[0]+' Semester Result.jpeg' # concatenating to get the new path
	#print(new_path)
	os.rename(i,new_path)#renaming

#to delete a file
#steps->
	#make the location available.
os.remove("//home/spyrustam/Desktop/Project_1\NewFlder")