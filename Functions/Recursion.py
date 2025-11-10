# Calculate the factorial of a number

def fact(n):
    if n == 0:
        res= 1
    else:
        res= n * fact(n-1)
    return res
print(fact(5))

def f(m):
    if m ==0:
        return 1
    else:
        return m*f(m-1)
print(f(4))

def fac(k):
    if k == 0:
        return 1
    else:
        return k*fac(k-1)
print(fac(9))