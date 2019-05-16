# finding GCD using Eculid's algorithm

def gcd(a,b):
    while (b !=0): # loop till we get 0
        t = b
        b = t % b
    return a
print(gcd(10,20)) # selct the numbers to find gcd