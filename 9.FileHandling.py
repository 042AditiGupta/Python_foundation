#File Handling
#Any name with an extension is file

# File handling means creating,Reading,Updating , Deleting (CRUD) operations that we can perform in files

a=open(r"C:\Users\ASUS\Downloads\bill.txt")
print(a.read())
a.close()

# a=open(r"C:\Users\ASUS\OneDrive\Desktop\Aditi-Coding\Python\BasicPython\day05.py")
# print(a.read())
#Default mode is read mode

r=open("superman.txt",'w')
r.close()
print(r.mode)
print(r.closed)
print(r.name)
#f.closed: Returns a boolean value- False when file is currently open otherwise True.
#f.mode: Tells us the mode in which the file was opened. Here, it’s 'r' which means read mode.

