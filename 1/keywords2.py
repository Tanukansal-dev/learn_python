# keywords
# Keywords are reserved words in Python that have special meaning and cannot be used
# as variable names, function names, or identifiers.
# They are part of the Python language syntax.


# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
#  'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
#  'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
#  'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))


# del keyword -
m = 10
print(m)
# del m
m = None
print(m)


# d = 50
# e = 50
d = e = 50
print(d)
print(e)