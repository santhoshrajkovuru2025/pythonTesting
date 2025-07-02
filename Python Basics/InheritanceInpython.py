from OOPSbasics import Calculator


class childClass(Calculator):

    num2=200

    def __init__(self):
        Calculator.__init__(self, 6, 8)


    def getComplete(self):
        return self.num2 + self.num + self.Summation()


obj=childClass()
print(obj.getComplete())




