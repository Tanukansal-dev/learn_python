# duplicates keys not allowed
# duplicates value are allowed
# mutable
# indexing and slicing are not allowed
# key --> gateway, value
# also use    d = ()

d = dict()
d[100] = "tanu"
d[200] = "kannu"
d[300] = "kansal"
print(d)
print(type(d))

print(d[200])

# update data from the dictionary -

d1 = {1:"tanu" ,2:"aadi" , 3:"vidhi"}
print(d1)
d1[2] = "pankaj"
print(d1)

# delete data -
del d1[3]
print(d1)

d1.clear()     # remove all
print(d1)

# functions- len(), clear(), d.get(key) <=> d[key](return -none) , d.get(key,default value)-(return default value)
d2 = {1:"tanu" ,2:"aadi" , 3:"vidhi"}
# print(len(d2))
# # d2.clear()
# print(d2)
#
# # print(d2.get(2))
# # print(d2[200])      # key error
# # print(d2.get(20))   # none
#
# print(d2.get(2,10))
# print(d2.get(20,10))

# print(d2.pop(2))
# print(d2.popitem())
# print(d2)

d3 = d2.copy()
print(d3)

d2.update({2:"hello"})
print(d2)


# dictionary comprehension -->
m = {x:x*x for x in range(1, 6)}
m1 = {x:2**x for x in range(1, 6)}
m2= {x:3**x for x in range(1, 6)}
print(m)
print(m1)
print(m2)

#problem -
word = "mississippi"
d5 ={}

for x in word:
    d5[x] = d5.get(m,0)+1

print(d5)