#some operations of set
A={1,2,3,4,5}
B={3,4,5,6}

union_set=A.union(B)
print(union_set)

#or we can write with pipe operation
print("using pipe operation is:")
print(A|B)

intersection_set=A.intersection(B)
print(intersection_set)

#or we can write like
print("and operation is:",A&(B))

difference_set=A.difference(B)
print(difference_set)

#symbol of difference is: '-'
print("difference of A and B using minus is sign is",A-B)

symmetric_diff=A.symmetric_difference(B)
print(symmetric_diff)

#symbol of symmetric_difference is
print("Symmetric difference is",A^B)

#Dictionary powers are like hashMap
#mutable,duplicates-key must be like unique,heterogenous


d={1:"heii"}
print(d)
print(type(d))

#dictionary-mutable(we can add or remove the values),keys must be unique,values can be common
# dictionary follow insertion order,heterogenous nature hota hai

d={10:100,20:200}
print(d)

#accessing element in dictionary
print(d[10])
print(d[20])

#We can also perform crud operations
#we can update values
d[10]=1000
print(d)

d.update({3:300})#updating
print(d)

del d[10] #delete
print(d)

d[40]=400#creating
print(d)

#Traversing in dictionary
for i in d:
    print(i,d[i])
    
# help(dict)

#remove all items from dictionary
# d.clear()
# print(d)

#Shallow and Deep copy

#Deep copy :
a=[1,2,3,4,5]
b=a
b[0]=100
print(a)

#shallow copy
a=[12,13,14,15]
b=a.copy()
print(b)
# a[0]=98
# print(b)

#get function
d={10:100,20:200,30:300}
print(d)
d2=d.get(20)
print(d2)

print(d.items()) #dict_items([(10, 100), (20, 200), (30, 300)])


# In Python dictionaries, both pop() and popitem() methods remove an item, 
# but pop() removes a specific item by its key, while popitem() removes the last inserted item. 


# d.popitem()
# print(d)

# d.popitem()
# print(d)

d.pop(10)
print(d)


#Write a python to merge two python dictionaries
d1={1:10,2:20,3:30}
d2={4:40,5:50,6:60}
d1.update(d2)
print(d1)

#write a python program to sum all the values in a dictionary

def sum(d1):
    val=0
    for i in d1:
        val+=i
    return val    
result=sum({1:10,2:20,3:30})
print(result)  


#count the frequency of each element

d1={1:200,2:300,4:400,1:300}
d2={3:20,4:500,1:300,2:87}
common=[]
for i in d1.keys():
    for j in d2.keys():
        if i==j:
            common.append(i)
print("All the common values")            
print('common values are',set(common))   


#other way to find common element
d1 = {1:200, 2:300, 4:400}
d2 = {3:20, 4:500, 1:300, 2:87}
common_keys = set(d1.keys()) & set(d2.keys())
print("common values are", common_keys)


#to combine common two dictionary by adding values of common keys
d1={1:10,2:20,3:20}
d2={3:10,4:20,1:10}
res={}
for i in d1:
    if i in d2:
        res[i]=d1[i]+d2[i]
print(res)           

