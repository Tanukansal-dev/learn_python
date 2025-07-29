# immutable
# same as list
# tuple is read only version of list
# ()bracket , separated by comma
# duplicates ae allow


# t = ()
# print(t)
# print(type(t))
t = (10,)
print(t)
print(type(t))

# access data -
# index
m = (10,20,30,40,50,60)
print(m[0])
print(m[-1])

#slice operator
print(m[2:5])

#immutable -
# m[0] = 1

# important function in tuple -
# except ---> append , insert, remove, pop, extend

# function -
h = (1,2,10,11,3,4,5,6,7,8)
print(len(h))
print((h.index(3)))
print((h.count(5)))
print(sorted(h))      # assending order


#tuple packing and unpacking -
# packing is the process of combining multiple values into a single tuple in a single statement.
#unpacking is process of assigning the value from a tuple to multiple variables in a single statement.
# unpacking is the reverce process of tuple packing.


f = 10,20,30,40,60,20  # tuple packing

g = 10
l = 20
k = g,l   # tuple packing

t = (10,20,30)
a,b,c = t       # unpacking tuple


# tuple comprehension --> not supported in python



























