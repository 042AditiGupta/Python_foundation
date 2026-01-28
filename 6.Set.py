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
s.discard(1)
print(s)
s.clear()
print(s)

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
