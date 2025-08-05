
 # Tuple:
 # Is a list data structure which is immutable i.e., can't be modified. Maintains the insertion order.
 # Duplicates are allowed
 # Different types of data are allowed(int, str,boolean, --- etc.).
 # Tuple type list is allowed when the read only and when there is a need of unmodified data is used in program.
 # if a tuple contains only single value for eg: tpl=(20,), then it should be always ', (comma)'  is used.
 # '()' is used to create a Tuple.

tpl = (1.0,2.0,11,22,33,"strange",'K')

print(tpl) # prints the tuple set
print(tpl*3) # prints the tuple list 3 times
print(type(tpl)) # prints the type of set
print(len(tpl)) # prints the length of the tuple
print(tpl[3]) # prints the given index
print(tpl.count(20))
print(tpl.index(33))


# list can be converted to the tuple.

lst = [1,2,3,4,5,6,7,8,9,10]
print(type(lst))
tp=tuple(lst)
print(tp)
print(type(tp))


