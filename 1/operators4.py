# An operator is a symbol or keyword that performs an operation on variables or values
print("arithmatic")
a = 10
b = 2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)     # ** square


print("relational or comparison and equality")
c = 10
d = 2

print(c<d)
print(c>d)
print(c<=d)
print(c>=d)
print(c==d)
print(c!=d)


m = False
n = True
print(m and n)
print(m or n)
print(not n)

print("assignment")
p = 10
t = 20
# p = p+20
# t = t-10
p+=20
t-=10
print(p)
print(t)

# ternary or conditional
r = "tanu" if 10>5 else "kansal"
print(r)

# identity
h = 10
g = 10
print(id(h))
print(id(g))
print(h is g)
print(h is not g)

#membership (check the presence)
u = [1,2,3,4]
print(10 in u)
print(10 not in u)
print(4 in u)


