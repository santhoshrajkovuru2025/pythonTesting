class Calculator:
    num=100

    # default Constructor
    def __init__(self):
        print('I am a default constructor')

    def getData(self):
        print('I am a Method')

obj = Calculator() # syntax to create the objects in python
obj.getData()
print(obj.num)



