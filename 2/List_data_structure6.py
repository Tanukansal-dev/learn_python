# holds multiple values in single container
# duplicates are allowed , mutable
# index --> +,-
# square bracket , separated by comma

list_1 = []
print(list_1)
print(type(list_1))

list_2 = ["tanu" , "kansal" , 2000000 , 123456789 ,"apple"]
print(list_2)
print(type(list_2))

#index
print(list_2[0])
print(list_2[-1])

# slice - list(start:end:step)
print(list_2[1:3])
print(list_2[1:4:2])

# list mutable

list_2[0] = "kiwi"
print(list_2)


# traversing
for x in list_2:
    print(x)

#function on list-

a = [10,20,30,40,50,60,20,20]
print(len(a))
print(a.count(20))
a.insert(2,"tanu")   # add item specific index
print(a)
a.extend([100,200])    # add list to another list
print(a)
a.remove(20)
print(a)
a.pop()       # remove last item
print(a)
print(a.pop(3))
print(a)

b = [1,2,3,4,5,6,10,7,9]
b.reverse()     # reverse list
print(b)

b.sort()      # ascending order for no.  , alphabetic order for string
print(b)

b.clear()      # clear list
print(b)

# removing multiple items -
c = [1,2,3,4,5,6,7,8,9]
items_to_remove = [1,3,4,5,6]

for item in items_to_remove:
    if item in c:
        c.remove(item)

        print(c)


# operators- concatenation and repitation
x = [1,2,3,4,5]
y = [10,20,30,40]
print(x+y)
print(x*10)
print(10 in x)
print(10 in y)
print(10 not in x)
print(10 not in y)

# nested list - list another list
z = [1,2,[3,4],5,6,[7,8,9]]
print(z)
print(z[2])
print(z[2][0])