# A function is a block of code which only runs when it is called.
def x():
 print("tanu kansal")
 print("tanu kansal")
 print("tanu kansal")
 print("tanu kansal")
 print("tanu kansal")

x()
x()

def my_function():
 print("Hello from a function")

my_function()  # call func

# types of function
#built In - print(), id(),type(),eval(),int(),etc.
#user defined functions- programmers develop func explicitly according to bussiness requirements

# syntax -

# def function( inputs or parameters):
#        statement1
#        statement2...
#        return result

# inputs or parameters and return --> optional

def function(name):
   print(f"hello tanu {name}")  # f-string me embed krne k liye


function("kansal")
function("bansal")
function("jindal")

# no arguments no return value
# with arguments no return value
# with arguments with return value
# no arguments with return value

# no arguments no return value
def myfunc():
  print("hello")

myfunc()
print(myfunc())


# with arguments no return value

def funct(name):
  print(f"hello tanu {name}")

funct("kansal")
print(funct("kansal"))


# with arguments with return value

def myfun(name):
   return f"hello tanu {name}"


myfun("kansal")
print(myfun("kansal"))


# no arguments with return value
def my_fun():
    return f"hello tanu"

my_fun()
print(my_fun())



def my(name):
    print("hello",name)

my("tanuk")

# exmaple-
def cal(a,b):
    return (a+b)

# sum = cal(10,20)
# print(sum)
print(cal(100,20))


#example-
def call(a,b):
    print(a+b)

call(10,30)


global_var = 20      # global variable

def func():
    local_var=10     # local variable
    print(local_var)
    print(global_var)

func()

# print(local_var)  -- valid
# print(global_var)  -- invalid
#example-

xy = 100           # global
def cool():
    xy = 200
    print(xy)       # local

cool()

#example-
xy = 100           # global

def cool():
    global xy
    xy = 200        # now it is global
    print(xy)

cool()

# types of arguments=================== positional arguments, keywords arguments
def func(i,j):
    print(i,j)

func(10,20)    # positional arguments
func(j=20,i=10)     # keywords arguments,when order is not imp

#example-

def func(i,j=10):
    print(i,j)

func(100,200)
func(100)