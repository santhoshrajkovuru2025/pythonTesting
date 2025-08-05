list = [1,2,3, "sam",20.5,-10,8]

print(list) # prints the list
print(list[3]) #prints the given index
print(list[1:6]) # prints the values in the list for the given range
print(list*5) # prints the values in the list multiple times
print(len(list)) # prints the length of the list
list.append(47) # Adds the data in the list
print(list)
list.remove("sam") # removes the data in the list
print(list)
del(list[2])
print(list)
# list.clear() --> clears the list.
print(max(list)) # prints the max value
print(min(list)) # prints the min value

list.insert(5,9) # Inserts the value in required index
print(list)
list.sort(reverse=True) # sorts the values in the list in reverse order.
print(list)


