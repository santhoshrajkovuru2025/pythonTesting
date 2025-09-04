dict={1:"James",2:"Ban",3:1,4:"Neem"}
print(dict)
print(dict.items())
print(dict.values())

# to print the keys
k=dict.keys()
for i in k:print(i)

# to print the values

v = dict.values()
for i in v:print(i)

# to print only value

print(dict[3])

# to delete
del dict[3]
print(dict)