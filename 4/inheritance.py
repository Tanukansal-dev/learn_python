# allows us to define a class that inherits all the methods and properties from another class.
# parent class -- base class, super class
# child class -- sub class, derived class

# objective of inheritance-
# use for reusability
# avoid duplication

# types -
# single
# multi level
# heirarchy
# multiple
# hybrid



# single -->
# class A:
#     def m1(self):
#         print("this is m1 from class A")
#
# class B(A):
#     def m2(self):
#         print("this is m2 from class B")
#
# b = B()
# b.m1()
# b.m2()



# multilevel-
# class A:
#     x,y = 10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b = 200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(B):
#     i,j= 5,2
#     def m3(self):
#         print(self.i*self.j)
#
#
# c=C()      # c is object
# c.m1()
# c.m2()
# c.m3()



# heirarchy-
# class A:
#     x,y = 10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b = 200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A):
#     i,j= 5,2
#     def m3(self):
#         print(self.i*self.j)
#
#
# b=B()
# b.m1()
# b.m2()
#
# c=C()
# c.m1()
# c.m3()



# multiple-
# class A:
#     x,y = 10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B():
#     a,b = 200,100
#     def m2(self):
#         print(self.a-self.b)
#
# class C(A,B):
#     i,j= 5,2
#     def m3(self):
#         print(self.i*self.j)
#
#
# c=C()
# c.m1()
# c.m2()
# c.m3()


# overriding-
# class parent():
#     name = "tanu"
#
# class child(parent):
#     name = "kansal"
#
# c=child()
# print(c.name)

# example -
# class bank:
#     def roi(self):
#         return 0
#
#
# class xbank(bank):
#     def roi(self):
#         return 10
#
# class ybank(bank):
#     def roi(self):
#         return 12
#
# x=xbank()
# print(x.roi())
#
# y=ybank()
# print(y.roi())



# polymorphism---we can implement using overloading concept
class human:
    def sayhello(self,name=None):
        if name is not None:
            print("hello" +name)
        else:
            print("hello")

h = human()
h.sayhello()             # else
h.sayhello("mini")       # if























































