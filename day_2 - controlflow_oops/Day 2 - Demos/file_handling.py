# File Handling in Python:

""" 
Python too supports file handling and allows users to handle files i.e., 
to read and write files, along with many other file handling options, to operate on files. 
The concept of file handling has stretched over various other languages, but the implementation 
is either complicated or lengthy, but like other concepts of Python, this concept here is also
easy and short. Python treats files differently as text or binary and this is important. 
Each line of code includes a sequence of characters and they form a text file. Each line of a
file is terminated with a special character, called the EOL or End of Line characters 
like comma {,} or newline character. It ends the current line and tells the interpreter 
a new one has begun. Let’s start with the reading and writing files. 

Before performing any operation on the file like reading or writing, first, we have to open that 
file. For this, we should use Python’s inbuilt function open() but at the time of opening, we have
to specify the mode, which represents the purpose of the opening file.

Eg. file=open("File_name","mode")

    file.close()---> The close() command terminates all the resources in use and frees the system of this particular program.

    To rename the file
    import os
    os.rename ("old name","new name")
    os.remove("file nmae")

where the following modes are supporting 

 1) r: open an existing file for a read operation.

 2) w: open an existing file for a write operation. If the file already contains some data then it will be overridden
    (It will errase the previous data and write the given coment in write/w mode ).

 3) a:  open an existing file for append operation. It won’t override existing data.

 4) r+:  To read and write data into the file. The previous data in the file will be overridden

 5) w+: To write and read data. It will override existing data.

 6) a+: To append and read data from the file. It won’t override existing data.

"""
# Reading modes of file 
Eg,

file=open("My.txt", "r")  #It will open the file My.txt in read mode. 
for each in file:         # Tjis will print each and every line in the  file.
    print(each)


# Another way of reading the file 
#Eg,

file= open("My.txt", "r")
print(file.read())

# Another way to read a file is to call a certain number of characters like in the following 
#code the interpreter will read the first five characters of stored data and return it as a string:

Eg,

file=open("My.txt","r")
print(file.read(10))  #It will read only 10 characters from the begianing of the data.and

# Writing modes of file:

"""
Let’s see how to create a file and how to write mode works, so in order to manipulate the file
"""
Eg,

file=open("My.txt","w+")

file.write("This is the added line in another mode ")  #In "w", "r+" and "w+" mode it will errase the previous data and add the given comment.
file.write("We can do like this ")
file=open("My.txt","r")
print(file.read())


# Append mode:

file=open("My.txt","a")
file.write("This is the appended line which will not distrub the existing data.")
file=open("my.txt","r")
print(file.read())

file=open("My.txt","r")
file.lstrip() 


# How to change a content of a file and save it in the same file ?

ds= open("text.txt",'r',encoding="utf8")
ds_content=ds.read()    # We are reading the  content of a file in a variable.

ds_content=ds_content.replace('data','rocket')    # Replacing the content in the same variable 
print(ds_content)
ds_w= open("text.txt",'w')    # Saving that variable in the same file.
ds_w.write(ds_content)      # content of file has been change in the same file successfully.
ds_w.close()




