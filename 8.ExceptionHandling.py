#Error
#1.syntax error
#2.Indentation error


a=12
if a==12:
    print("hello")
#Exception are unexpected events or errors that occurs during the
#execution of a program,which disrupts the normal flow of the program

#a=int(input("tell your number:"))
#print(10/a) #ZeroDivisionError: division by zero if divide by 0
#print("ok i havee done the divison")

#print(10/0) get error

#Exceptional handling

# try- wrap the block that might cause an exception
# except- handle the exception if it occurs

a=int(input('tell your number'))
try:
    print(10/a)
except ZeroDivisionError:
    print("sorry u cannot divide by 0") 
else:
    print("good there is no exception")  
finally:
    print("I will run on matter what")
           
print("ok i have done the divison")


#Finally block will always run 

# raise- manually throw an exception

age=int(input("enter your age:"))
try:
    if age<10 or age>18:
        raise ValueError("sorry! your age must be between 10 and 18")
    else:
     print("welcome to the club")
except Exception as err:
    print(f"an error occurred as {err}")   
print("the club will start soon")

