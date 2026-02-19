""" Anonymous functions are also known as Lambda functions
 This functions are not defined by def keyword
 This functions cannot access global variables
 Return expression but not value
 This functions are one line functions
 This functions can use any number of arguments
 These are defined by Lambda Keyword
 These functions doesn't have any name

 syntax:
 lambda arguments : expression
 """

sum = lambda x, y,z,m,n: x + y*z/m%n
print(sum(1,2,3,5,4))

