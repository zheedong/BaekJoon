def gcd(a, b):
    if  (b == 0):
        return a
    else:
        return gcd(b, a%b)
        
def lcm(a, b):
    return a*b / gcd(a,b)

a, b = input().split()
a = int(a)
b = int(b)

print(gcd(a, b))
print(int(lcm(a, b)))
