
#comment - single line
"""Doctstring- Hello this is multi line..when we need paragraph"""

MyName="Aditi" #pascal case

myName="Aditi" #camel case

my_name="Aditi" #snake case


#Datatype-number,String,boolean (for Now)
#1.Numbers:Int,float,complex

#Int
a=12
print(type(a))


#Float- any floating number and no in the form of p/q
b=56/8
c=4.5

#complex- Imaginary value (i:iota)
v=34j
print(type(v))

#String
st='123adiitlet'
print(type(st))

#boolean
b=True
print(type(b))

a='A'
print(ord(a)) #unicode - 65

a=65
print(chr(a)) #character - a

#indexing
a='HERO'
print(a[3])
print(a[-1])

#slicing in python
a='SHER CODER'
print(a[0:4:1]) #start,stop and steps
print(a[5::1])

#Type conversion - Explicit Type conversion
#int(),str(),bool(),float()
a=12
print(type(a)) #<class 'int'>

a=(str)(a)
print(type(a)) #<class 'str'>

a="12"
a=int(a)
print(type(a))

#Truthy values and falsy values - 7
#Falsy values are : 0,0.0,[],(),{},"",False
a=0
print(bool(a))


# Two type of type conversion-explicit and implicit

#Formatted string
name="aditi"
age=22
print(f"my name is {name} and my age is {age}")

#Input and output in python
#age=input('enter your age')
#print(age)

#Operators - 7 Types : +,-,*,/,%,//,**
a=12
b=20
print(a+b)
print(b-a)
print(a*b)
print(b/a) # float divison
print(b//a) #floor divison - give results in integers
print(5**2)
print(3%2)

#python follows BODMAS

#Assignment operator
#a=23

#Compound assignment operations
a=20
a+=20
a+=40
print(a)

#comparison opertor - 6 types of comparison
a=12
b=12
print(a==b)
print(a!=b)
print(a<b)
print(a>b)

#Logical operator
print(123>100 and 123>45 and 34==34)
print(not 12==12)

#Conditional statement
#taskA<10

a=13
if a>10:
    print('I will do task A')
else:
    print('I will do task B')   

#if elif:
money=int(input('enter the money'))
if money==10:
    print('I will have mango icecream')
elif money==20:
    print('I will have choco icecream')
else:
    print('I will have cone')

#Some questions on conditional
#1.Accept two numbers and print the largest between them
a=int(input('enter first number'))       
b=int(input('enter second number')) 
if a>b:
    print('a is largest')
else:
    print('b is largest')
    
#2.Accept gender from the user as char and print the respective greeting message
a=input("enter the gender")
if a=='male' or a=='m':
    print('good morning sir')
else:
    print('good morning mam')    

#3.Accept an integer and check whether it is an even number or odd
a=int(input('enter the value'))
if a%2==0:
    print('even number')
else:
    print('odd number')    

#4.Accept name and age from the users .Check if the user is a valid voter or not.
name=input("Enter the name")
age=int(input('Enter the age'))
if age > 18:
    print('yes! the person is eligible for vote')
else:
    print('Sorry! not eligible')    
    
#5.Accept a year aand check if it is a leap year or not
year=int(input('enter the leap year'))
if (year % 400 ) or (year % 4 ==0 and year % 100 != 0):
    print('yes! Its leap year')
else:
    print("not leap year")  

#if - elif ladder
temp=int(input('enter the temperature'))
if temp<10:
    print('Freezing Cold')
elif temp>=0 or temp<11:
    print('Very Cold')    
elif temp>=10 or temp<20:
    print('Cold')
elif temp>=20 or temp<30:
    print('Hot')      

