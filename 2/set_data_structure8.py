# set --> group of unique values as a single entity
# duplicates are not allowed
# insertion , indexing, slicing is not allowed
# mutable
# {}

# s = {}   gives - dict
s = set()    # empty set
print(type(s))

s1 = {10,20,30,40,50} # empty set
print(s1)
print(type(s1))

# duplicates are not allowed-
s2 = {10,10,20,3,4,3,5,5,7,8,7,8}
print(s2)

# function of set -
s3 = {1,2,3,4,5}
s3.add(40)
print(s3)

s3.update([40,50,50])
print(s3)

s3.copy()    # clone
print(s3)

s4 = {1,2,3,4,5,6,7}
s4.pop()
print(s4)
s4.clear()
print(s4)


# mathematical operations-union(), intersection(),difference(), symmetric_difference()
x = {10,20,30,40}
y = {30,40,50,60}
print(x.union(y))
print(x.intersection(y))
print(x.difference(y))
print(x.symmetric_difference(y))