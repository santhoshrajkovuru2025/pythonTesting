
x=111

def display():
    x=222
    print(x)
    print(globals()['x'])

print(x)
z=display
z() # used to assigning the function to  variable and should be called