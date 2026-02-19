class Course:
    def __init__(self,name,price,ratings,author):
        self.name= name
        self.price= price
        self.ratings= ratings
        self.author= author

c=Course("python",479,[1,2,3,4,5],"vamshi")
print(c.name)
print(c.price)
print(c.ratings)

c1= Course("java",500,[1,2,3,4,5],"Ravi")
print(c1.name)
print(c1.price)
print(c1.ratings)

