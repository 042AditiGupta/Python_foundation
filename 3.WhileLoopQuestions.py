
#return all the methods
#print(dir(str))
#print(dir(int))

#while loops - works on condition
i=0
while(i<10):
    print(i)
    i+=1
    
#separate each digit of a number and print it on the new line
a=198
while(a!=0):
    r=a%10
    print(f"{r}")
    a=a//10

#print reverse of a number
b=123
rev=0
while(b!=0):
    a=b%10
    rev=rev*10+a
    b=b//10
print(rev)   

#accept a number and check if it is palindrome number
num=121
check=num
rev=0
while(num>0):
    r=num%10
    rev=rev*10+r
    num=num//10
if(rev==check):
    print('yes  it is palindrome')   
else:
    print('not palindrome') 

#create a random number guessing game with python
import random
num=random.randint(1,11)
guess=int(input("please guess your number:"))  
if num==guess:
    print("you are right")  
else:
    print("sorry you are wrong")    
    

