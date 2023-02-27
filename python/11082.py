from math import gcd

inp = input()

try:
    integer, decimal = inp.split(".")
    integer = int(integer)
    decimal = int(decimal[1:-1])

    up = int(str(integer) + str(decimal)) - integer
    down = int(10 ** len(str(decimal))) - 1
    common = gcd(up, down)
    print(f"{up // common}/{down // common}")
except:
    integer, decimal = int(inp), None
    print(f"{integer}/1")

# x.ab(123)

try:
    integer, decimal = inp.split(".")
    integer = int(integer)
    if decimal[0] == "(":
        decimal = int(decimal[1:-1])

        up = int(str(integer) + str(decimal)) - integer
        down = int(10 ** len(str(decimal))) - 1
        common = gcd(up, down)
        print(f"{up // common}/{down // common}")
    else:

except:
    integer, decimal = int(inp), None
    print(f"{integer}/1")
