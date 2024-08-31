
name="Suman Saurav"
for _ in range(3):
    print(name)

# Suman Saurav
# Suman Saurav
# Suman Saurav

for i in range(3):
    print(name)
 
# Suman Saurav
# Suman Saurav
# Suman Saurav

for i in range(3):
    print(i)

# 0
# 1
# 2

# help(range)

# Help on class range in module builtins:

# class range(object)
#  |  range(stop) -> range object
#  |  range(start, stop[, step]) -> range object
#  |
#  |  Return an object that produces a sequence of integers from start (inclusive)
#  |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
#  |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
#  |  These are exactly the valid indices for a list of 4 elements.
#  |  When step is given, it specifies the increment (or decrement).
#  |
#  |  Methods defined here:
#  |
#  |  __bool__(self, /)
#  |      True if self else False
#  |
#  |  __contains__(self, key, /)
#  |      Return bool(key in self).
#  |
#  |  __eq__(self, value, /)
#  |      Return self==value.
#  |
#  |  __ge__(self, value, /)
#  |      Return self>=value.
#  |
#  |  __getattribute__(self, name, /)
#  |      Return getattr(self, name).
#  |
#  |  __getitem__(self, key, /)
#  |      Return self[key].
#  |
#  |  __gt__(self, value, /)
#  |      Return self>value.
#  |
#  |  __hash__(self, /)
#  |      Return hash(self).
#  |
#  |  __iter__(self, /)
#  |      Implement iter(self).
#  |
#  |  __le__(self, value, /)
#  |      Return self<=value.
#  |
#  |  __len__(self, /)
#  |      Return len(self).
#  |
#  |  __lt__(self, value, /)
#  |      Return self<value.
#  |
#  |  __ne__(self, value, /)
#  |      Return self!=value.
#  |
#  |  __reduce__(...)
#  |      Helper for pickle.
#  |
#  |  __repr__(self, /)
#  |      Return repr(self).
#  |
#  |  __reversed__(...)
#  |      Return a reverse iterator.
#  |
#  |  count(...)
#  |      rangeobject.count(value) -> integer -- return number of occurrences of value
#  |
#  |  index(...)
#  |      rangeobject.index(value) -> integer -- return index of value.
#  |      Raise ValueError if the value is not present.
#  |
#  |  ----------------------------------------------------------------------
#  |  Static methods defined here:
#  |
#  |  __new__(*args, **kwargs)
#  |      Create and return a new object.  See help(type) for accurate signature.
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  start
#  |
#  |  step
#  |
#  |  stop

for i in range(1,5):
    print(name)

# Suman Saurav
# Suman Saurav
# Suman Saurav
# Suman Saurav
for i in range(1,5):
    print(i)
   
# 1
# 2
# 3
# 4

# dir(list)

# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# 1_5=list(range(10))
# SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
# 1_5==list(range(10))
# False
# 1_5
# 15
# 1_5=list(range(10))
# SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
# 1_5
# 15
# arr=list(arnge(5))
# Traceback (most recent call last):
#   File "<pyshell#20>", line 1, in <module>
#     arr=list(arnge(5))
# NameError: name 'arnge' is not defined. Did you mean: 'range'?

arr=list(range(5))
# arr
# [0, 1, 2, 3, 4]

for i in range(2,5,7):
    print(i)
   
# 2

for i in range(2,5,2):
    print(i)
    
# 2
# 4

for i in range(2,20,5):
    print(i)
  
# 2
# 7
# 12
# 17

for i in range(2,20,2):
    print(i);

# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18

for name in arr:
    print(name)

# 0
# 1
# 2
# 3
# 4

len(arr)
# 5

5+7
# 12
15/5
# 3.0
6//2
# 3
5/3
# 1.6666666666666667
5%2
# 1
for i in arr:
    print(i*2)
   
# 0
# 2
# 4
# 6
# 8

for i in arr:
    print(i)
    print(i*2)
    print()

    
# 0
# 0

# 1
# 2

# 2
# 4

# 3
# 6

# 4
# 8

name="Suman";
print(len(name))
# 5

name[0]
# 'S'
name[0:4]
# 'Suma'
name[:3]
# 'Sum'
name[0:]
# 'Suman'
name[::2]
# 'Smn'
name[:]
# 'Suman'
name[::-1]
# 'namuS'
name[1:5]
# 'uman'
"p"+name[:1]
# 'pS'
"P"+name[:3]
# 'PSum'
"P"+name
# 'PSuman'
"P"+name[:]
# 'PSuman'
for i in name:
     print(i+name[1:])

    
# Suman
# uuman
# muman
# auman
# numan

for i in name:
    print(i)

    
# S
# u
# m
# a
# n

for i in name:
     print(i+name[1:])

     
# Suman
# uuman
# muman
# auman
# numan
friends="ROHAN"
for i in friends:
     print(i+name[1:])
 
  
# Ruman
# Ouman
# Human
# Auman
# Numan
