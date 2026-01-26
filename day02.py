#Loops in Python
# 2 loops in python : for loop, while loops 
# difference between for and while loops:
# for loop works on number and while loop works on any condition

# print("hello world")
#for loop
#range(start,stop,step)

a=range(1,20,1)

# for i in a:
#     print(i)

# -3 to -15
for i in range(-3,-16,-1):
    print(i)   

#16 to 1
for i in range(16,0,-1):
    print(i) 
    
#Loops in strings
# a="Nature is very pure and natural"
# print(len(a))
# for i in range(len(a)):
#     print(a[i])
    
a="aditi"
for char in a:
    print(a)
    
#break
for i in range(1,21):
    if i==15:
        break
    print(i)
    
#continue
for i in range(1,21):
    if i==15:
        continue
    print(i)
    
#if-else
for i in range(1,21):
    if i==56:
        print("break statement is executed")
        break
    print(i)
else:
    print("Break statement is not executed")
    
#Accept an integer and print hello world n times
n=int(input('enter a number'))
for i in range(n):
    print('hello world')
    
#Print natural number upto n
num=int(input('enter a number to print natural number'))
for i in range(1,num+1,1):
    print(i)
    
#Reverse for loop.Print n to 1
rev=int(input('enter number to print its reverse'))
for i in range(rev,0,-1):
    print(i)
    
#Take a number as input and print its table
val=int(input('enter a number'))
print('table of val')
for i in range(val,val*10+1,val):
    print(i)
    
#sum up to n terms
sum=0
for i in range(0,val+1):
    sum+=i
print(sum) 

#factorial of a number
fact=1
for i in range(val,1,-1):
    fact*=i
print('factorial of a number is',fact)    

#print of sum of all even & odd numbers in a range separately
a=int(input('enter a number'))
sum_odd=0
sum_even=0
for i in range(1,a+1):
    if(i%2==0):
        sum_even+=i
    else:
        sum_odd+=i

print(sum_even)
print(sum_odd)    

# print all the factors of a number
num=int(input('enter a number to print its factor'))
for i in range(1,num+1):
    if num % i == 0:
        print(i)
        
# Accept a number and check if it a perfect number or not
# A number whose sum of factors is equal to the number itself
# Ex-6=1,2,3=6

num=int(input('enter a number to check it is perfect or not'))
chk=0
for i in range(1,num):
    if num % i == 0:
        chk+=i
    
if chk==num:
    print(num,'yes it is perfect number')  
else:
    print('not perfect')  

#check whether the number is prime or not

num=int(input('enter a number'))
cnt=0
if num<=1:
    print('not prime')
for i in range(1,num):
    if num%i ==0:
        cnt+=i
if cnt>2:
    print('not prime')
else:
    print('prime')    
    
#string reverse
name=input('enter the name')
rev_name=""
for ch in range(len(name)-1,-1,-1):
    rev_name+=name[ch]
print(rev_name)
    
#check if string is palindrome or not
str=input('enter the string')
rev_str=""
for i in range(len(str)-1,-1,-1):
    rev_str+=str[i]
if rev_str==str:
    print('palindrome hai')
else:
    print('not palindrome')        
    
#Count all letters,digits, and special symbols from a given string

str="P@#yn26at^&i5ve"
count_letter=0
count_digit=0
count_spesymbol=0
for i in range(len(str)-1,-1,-1):
    ascii=ord(str[i])
    if (ascii>=48 and ascii<=57):
        count_digit+=1
    elif (ascii>=65 and ascii<=90) or (ascii>=97 and ascii<=122):
        count_letter+=1  
    else:
        count_spesymbol+=1       
print(count_letter)
print(count_digit)
print(count_spesymbol)