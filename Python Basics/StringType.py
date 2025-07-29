s='   you are awesome  '
print(s)
s1="""You're the one
      product of the
      creator of the universe"""
print(s1)
print(s1[0]) # prints the zero value of the string
print(len(s1)) # length of the string
print(s[:8]) # prints the given range of the values till range ends.
print(s1[0:9:2]) #string slicing
print(s1[0:15:3]) # only prints the values given in the range
print(s1[20::-3]) #  only pints the given values of back front and reverse of the string.
print(s.strip()) #  clear the spaces from both the left and Right sides
print(s.lstrip())  # clear spaces only from the left side
print(s.rstrip()) # clear the spaces only from the right side

print(s.find("awe",0,len(s))) # prints the index of the string value.

print(s.find("awe"),0,len(s)) # prints the length of the string, given index and 0.

print(s.find("awe",0,8))
print(s.count("a")) # prints the count of the given character or string value
print(s.replace("awesome", "super")) # replaces the value.
print(s.upper()) # prints the value in upper case
print(s.lower()) # prints the value in lower case
print(s.title()) # prints the value in title case