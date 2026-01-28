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

