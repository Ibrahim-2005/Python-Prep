"""
open()  Opens the file
close()	Closes the file
read()	Returns the file content
readline()	Returns one line from the file
readlines()	Returns a list of lines from the file
seek()	Change the file position
tell()	Returns the current file position
write()	Writes the specified string to the file
writelines()	Writes a list of strings to the file

"""


f = open("C:\\Users\\ibrah\\OneDrive\\Documents\\Desktop\\PYTHON-PREP\\07.File_Handling.py\\example.txt")
txt = f.read()
print(type(txt))
print(txt,"\n")
f.close()


f = open("C:\\Users\\ibrah\\OneDrive\\Documents\\Desktop\\PYTHON-PREP\\07.File_Handling.py\\example.txt")
txt = f.read(10)            # print the first 10 characters of the text file.
print(txt,"\n")
f.close()


f = open("C:\\Users\\ibrah\\OneDrive\\Documents\\Desktop\\PYTHON-PREP\\07.File_Handling.py\\example.txt")
txt = f.readline()            # print the first line of the text file.
print(txt)
f.close()


f = open("C:\\Users\\ibrah\\OneDrive\\Documents\\Desktop\\PYTHON-PREP\\07.File_Handling.py\\example.txt")
txt = f.readlines()            # print the first line of the text file.
print(txt)
f.close()


f = open("C:\\Users\\ibrah\\OneDrive\\Documents\\Desktop\\PYTHON-PREP\\07.File_Handling.py\\example.txt","w")
f.write("Hello Ibrahim!\n")   # write text
f.close()


f = open("C:\\Users\\ibrah\\OneDrive\\Documents\\Desktop\\PYTHON-PREP\\07.File_Handling.py\\example.txt","a")
f.write("This is a new line.\n")
f.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])  # multiple lines
f.close()


f = open("C:\\Users\\ibrah\\OneDrive\\Documents\\Desktop\\PYTHON-PREP\\07.File_Handling.py\\example.txt","a")
pos = f.tell()   # current position
print("Cursor position at:", pos)

f.seek(0)       # move cursor back to start
curr=f.tell()       
print("After seek(),:", curr)
f.close()



with open("C:\\Users\\ibrah\\OneDrive\\Documents\\Desktop\\PYTHON-PREP\\07.File_Handling.py\\example.txt") as f:    # Automatically closes the file
    txt = f.read()          
    print(txt)