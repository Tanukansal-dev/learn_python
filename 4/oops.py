# python - structured + object oriented
#oops -
# class - collection of variables(attribute), blue print, does not occupy space in memory
# object
# inheritance
# polymorphism(overloading)
from tkinter.font import names


# crete class -
class myclass:
    def myfun(self):
        pass
    def display(self,name):
        print(name)

mc1 = myclass()
mc1.myfun()
mc1.display("kansal")

# two types of method- instance( call only through object) and static(directly call using class)
# example -2
class my_class:
    def m1(self):
        print("this is instance method")
    @staticmethod
    def m2(self,num):
        print(num)

mc = my_class()
mc.m1()
mc.m2(100,10)

my_class.m2(10,20)   # here calling directly using class


# example -
class clas:
    a,b = 30,40  # class variable
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)

mc = clas()
mc.add()
mc.mul()


# example-

i,j = 15,25                   # global

class myclass():
    a,b = 10,20               # class
    def add(self,x,y):
        print(x+y)            # x,y local
        print(self.a+self.b)
        print(i+j)

mc = myclass()
mc.add(100,200)



# method -
# give any names
# return the value
# can take arguments/parametres
# we have to use an object to invoke the method
#
#
# constructor-
# name is fixed
# def __init__(self)
# will not return the value
# also take arguments/parametres
# will be called at the time of object creation itself.


class myclass:
    def __init__(self):
        print("this is constructor")
    def m1(self):
        print("hello")
    def m2(self,x,y):
        return(x+y)

mc = myclass()      # constructor
mc.m1()             # method
print(mc.m2(10,20))


# eg-
class emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def display(self):
        print(self.eid,self.ename,self.sal)

e1= emp(101,'tanu',5000000)
e1.display()