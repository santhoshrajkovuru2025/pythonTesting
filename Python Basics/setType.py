'''
set:
'{}' is used to create a set type.
set does not support indexing and slicing
set does not support the duplication of values in printing the values
we have 'frozenset' that means we cant perform any operation on frozen set.
frozenset doesn't support the update and remove attributes
'''

s ={1,2,3,4,5,6,7,8,9,10,10,9,8}
print(s)
print(type(s))  # used to print the type of the list
s.update([11,12,13,14]) # is used to update the values
print(s)
s.remove(10)

f = frozenset(s)
print(f)

