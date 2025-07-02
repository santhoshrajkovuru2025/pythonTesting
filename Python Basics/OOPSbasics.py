##Notes:

# 'Self' keyword is mandatory for calling the variable names into the method
# Instance and class variables have whole different purpose
# Constructor name should be __init__
# 'new' keyword is not required for creation of object.


class Calculator:
    num=100

    # default Constructor
    def __init__(self,a,b):
        self.firstNumber=a
        self.secondNumber=b
        print('I am a default constructor')

    def getData(self):
        print('I am a Method')

    def Summation(self):
        return self.firstNumber+self.secondNumber+Calculator.num


obj = Calculator(5,6) # syntax to create the objects in python
obj.getData()
print(obj.Summation())


obj = Calculator(7,9) # syntax to create the objects in python
obj.getData()
print(obj.Summation())