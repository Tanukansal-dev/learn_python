# if  (conditional statement for one time)

# x = 10
# if x>5:
#  print("x is greater than 5")
#
#
#  name = input("enter name :")
#  if name == "tanu kansal" :
#        print("hello tanu ,how are u")


# else

# y = 10
# if y<5:
#  print("y is greater than 5")
#
# else:
#   print("y is not greater then 5")



# m = 3
# if m%2==0:
#      print("even number")
# else:
#      print("odd number")
#
#
# k = 104
# if k%2==0:
#      print("even number")
# else:
#      print("odd number")



# if-elif-else -


# marks = 85
# if marks>=90:
#      print("A grade")
# elif marks>=80:
#      print("B brade")
# elif marks>=70:
#      print("C grade")
# else: print("failed")


#numbers = input("enter numbers : ")

 # if numbers=="A":
 #      print("A grade")
# elif numbers=="B":
#      print("B brade")
# elif numbers=="C":
#      print("C grade")
# else:
#     print("failed")


# nested conditional statements-
#conditional statements inside another conditional statements

num = 5
if num>0:
     if num%2 == 0:
          print("positive and even number")
     else:
          print("positive and odd number")
elif num<0:
     print("negative number")
else:
     print("zero number")



 # iterative statements
 # while loop - (if we want to execute a group of statements multiple times )

# print number from 1 to 10 by using while loop-

i = 1            # initialization
while i<=10:     # condition
     print(i)
     i = i+1     # incrementation

# print numbers  from 10 to 1 by using while loop

h = 10
while h>=1:
     print(h)
     h = h-1


 #for loop with range function--
 #range function - generates sequence of numbers from start to end or stop
# range(stop)
# range(start,stop)
# range(start,stop,step)
# step - diff b/w each no. in the sequence
# range(100,200)- 100,101,102,103......199
#by default--> 1
# step --> +ve left to right
# step --> -ve right to left
# range(200,100,-1) --> 200,199,198......101
# range function --> range data type -- sequence of no. -- immutable(not modified)
print(".............................................")
print(range(10))
print(list(range(20)))
print(list(range(5,10)))
print(list(range(5,10,1)))
print(list(range(5,20,2)))

print(list(range(10,1,-1)))
print(list(range(10,1,1)))
print(list(range(10,15,-1)))

# for loop -
# print 1 to 10

for each_element in range(1,11):
      print(each_element)

# each_element = X (we can use simple variables)
for X in range(1,11):
      print(X)

  #print even number-

for u in range(2,21,2):
         print(u)

# print odd no. -

for X in range(1,21,2):
     print(X)

T = "tanu kansal"
for x in T:
     print(x)

for X in range(10):
     print("tanu kansal")

     # ---------- transfer statements ---------
print("..................................................")
cart = [10,20,600,60,70]
for item in cart:
     if item>550:
        print("to place this order, insurance must be required")
        break
     print(item)

print("..................................................")
cart = [10, 20, 600, 60, 70]
for item in cart:
          if item > 550:
               print("to place this order, insurance must be required")
               continue
          print(item)

print("..................................................")
cart = [10,20,600,60,70]
for item in cart:
     if item>550:
        print("to place this order, insurance must be required")
        pass
     print(item)