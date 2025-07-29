#A string is a sequence of characters enclosed in quotes.
#It is used to store text in Python.

s = "hello"
m= 'hello'
print(type(s))
print(type(m))

# multi line string literals- '''  ''' , """ """

k = '''welcome
        to
       python
     programming'''
print(k)



h = """welcome
        to
       python
     programming"""
print(h)

# we should never use same quotes inside same quotes.
# we can use opposite quotes.
# like - "welcome to "the" world".

# len() - returns count of characters
# index - n-1

p = "mango"
print(p[0])
print(p[1])
print(p[2])
print(p[3])
print(p[4])
print(p[-1])
print(p[-2])
print(p[-3])
print(p[-4])
print(p[-5])


# slice operator- The slice operator is used to extract a portion (substring/sublist)
# from a string, list, or tuple using index positions.

f = "abcdefghi world is very harsh"
print(f[1:6:2])
print(f[6])
print(f[6:])
print(f[::-1])       # reverse sentence

# mathematical operations-
# + concatenation operator --> compulsory both arguments must be string data type
# * repetition operator --> one argument must be string and other argument must be integer

s1 = "welcome"
s2 = "to the world"
s3 = s1+s2

print(s3)

s4 = s1*10
print(s4)
print(len(s2))
# len() --> counts number of characters in a string.



# substring in main string -->
# identity --> is, is not
# membership --> in, not in


# membership operator --> boolean value
print("to" in s2)
print("to" not in s2)


# remove spaces in string -
a = " hello "
print(a.rstrip())
print(a.lstrip())
print(a.strip())   # both remove


# find substrings -
#  find() --> index of first occurence of substring --> -1 if not found
#  index() --> same as find() --> error , if not found
#  rfind() --> index of last occurence of substring --> -1 if not found
#  rindex() --> same as rfind() -->  error , if not found


b = " python is very very simple "
print(b.find("very"))
print(b.rfind("very"))
print(b.index("very"))
print(b.rindex("very"))

# count() --> number of times a substring has occured in main string

print(b.count("very"))


# replace() --> replace substring in a main string

c = " i am best"
print(c)
c1 = c.replace('best' , 'bestest')
print(c1)

# string - we cannot modify data
# splitting and joining the strings -->

d = "learning python is easy"
l = d.split()
print(l)

r = ['apple' , 'mango' , 'kiwi']
r1 = "-".join(r)
r2 = "/".join(r)
print(r1)
print(r2)


# upper() -- convert all characters to upper case
# lower() -- convert all characters to lower case
# swapcase() -- convert all lower case to upper case and vice versa
# title() -- convert all characters to title case, i.e first character
#            in every word should be upper case and all remaining characters should be in lower case.
# capitalize() -- only first character will be converted to uppercase and all
#                 remaining characters can be converted to lower case.


g = ' learning PythoN is very easy'
print(g.upper())
print(g.lower())
print(g.swapcase())
print(g.title())
print(g.capitalize())