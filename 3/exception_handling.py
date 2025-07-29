#  is a way to manage errors that occur during the execution of a program

print("hello tanu kansal")
print("hello tanu kansal")
print("hello tanu kansal")

try:
   print(x)
except:
    print("exception occured")

print("hello")
print("hello")
print("hello")


# multiple except blocks -- try,except,else,finally
try:
    a,b =10,5
    c = a/b
    print(c)
except ZeroDivisionError:
    print("plz check")
except SyntaxError:
    print("syntax error")
except:
    print("exception handled")
else:
    print("no exception occured")
finally:
    print("always execute")


# except - executes only when exception occured
# else - executes only when exception not  occured
# finally - always execute

# example - raise

def enter_age(num):
    if num<0:
        raise ValueError("only + integers are allowed")
    if num%2==0:
        print("even")
    else:
        print("odd")

# enter_age(10)
# enter_age(0)
num = -1
try:
  enter_age(num)
except ValueError:
    print("exception occureddd ")
