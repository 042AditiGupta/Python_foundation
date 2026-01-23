#Tuple

a=(12,1,2,3)
#a[0]=9 , cannot change the value
#print(a)
#Tuples are immutable,

# Duplicate values # tuples can have duplicates value
print(a[2]) # for 2

# heterogeneous values
#Traversing in tuple:

#1st way
for i in a:
    print(i)

#2nd way
for i in range(len(a)):
    print(a[i]) 

#index
#count

b=(1,2,3,4,5,55,5,5,5,print(),"hello")
index=b.index(5)
print(index)

count=b.count(5)
print(count)

#Tuple unpacking
a,b,c,d=(1,2,3,4)
print(a)
print(b)
print(c)
print(d)

#Type of class- integer
a=(1)
print(type(a))

#Set
s={1,2,3,4,5}
#does not contain any duplicates,unordered
print(s)
s1={1,1,1,2,3,4,4,5,5}
print(s1)

# set is semi-heterogeneous 
#sets are unordered , all depends on hash code
#hash() function in python

b=hash("hello")
print(b)

s={1,2,3,4,5}
for i in s:
    print(i)

s.add(6)
print(s)   
s.remove(1)
print(s)


