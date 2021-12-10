import math

fact = str(math.factorial(int(input())))

print(len(fact) - len(fact.strip('0')))