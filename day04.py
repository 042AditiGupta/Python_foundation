# Functions in python
#Group reusable code into a block that can be executed by calling the function name
#print("hello how are you")
#def keyword
def hello():
    print("hii welcome to functions in python")
hello()   

#Parameters and arguments
def sum(a,b):
    print(f"The sum of your number is{a+b}")
sum(12,12)    

#here a,b are parameters, and 12,12 are arguments

#Types of arguments - Positional argument, default , and keyword argument

#1.Positional argument
def sum(name,age):
    print(f"The name is{name}")
sum("aditii",22)   

#Default argument
def fun(name,age=22):
    print(f"age is{age} and name is {name}")
fun("gouri")

#keyword argument
def greet(name,age):
    print(f"I am {name} and I am {age} years old")
greet(age=10,name="raatdin")   


# palindrome string
def palindrome(st):
    rev=""
    for i in range(len(st)-1,-1,-1):
        rev+=st[i]
    if  rev==st:
        print("yes palindrome") 
    else:
        print("not palindrome")       
palindrome("ili") 


#In-Built data structures are- List,Tuple,Dictionary and Set
#custom data structures are - Stack,Queue,Linked List and Graph

#List- A list is a collection which is ordered and changeable. Allows duplicate members.
a=[12,13,14,35.4,True]

print(a[0])#Accessing element in list
print(a[0:5])#slicing

#list traversing: #1st way uing index
for i in range(len(a)):
    print(a[i])
    
#2nd Directly on values
print("traversing using values")
for i in a:
    print(i)
    
#methods is kind of function defined inside the class
#print(dir(list))
#help(list)

l=[1,2,3,4,5]
l.append(9)
l.append(10)
l.insert(1,20)
print(l)
l.extend([23,89])
print(l)
l.remove(1) # removes first element
print(l)
count_5=l.count(3)
print(count_5)
l.reverse()
print(l)
new_numbers=l.copy()
print(new_numbers)
new_numbers.clear()
print(new_numbers)
popped_element=l.pop(1)
print(popped_element)
l[0]=90
print(l[0])


# Questions on list

#1.Print positive and negative elements of list

mylist=[1,2,3,4,-12,5,-8,-5,10,0]
print("positive numbers:")
for i in mylist:
    if(i>=0):
        print(i)
print("negative numbers are:")           
for i in mylist:
    if(i<0):
        print(i)

# mean of list element
sum=0
mean_ele=[1,2,3,4,15]
for i in mean_ele:
    sum+=i
print(f"mean of list element is: {sum/len(mean_ele)}")   

#Find the greatest element and print its index too.
max=0
for i in mean_ele:
    if(i>max):
        max=i
print(f"maximum greatest element is : {max}")  

# Find the second greatest element
mx=0
smax=0
for i in mean_ele:
    if(i>mx):
        smax=mx
        mx=i
    elif(i>smax and smax!=mx):
        smax=i     
print(smax)

#Check if List is sorted or not
mylist=[98,1,2,3,54,23,8]
li=[1,2,3,4]
def chksort():
    return mylist==sorted(mylist)
print(chksort())