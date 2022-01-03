a = int(input())
b = int(input())
c = int(input())

mul = list(map(int, list(str(a * b * c))))

for i in range(0, 10):
    print(mul.count(i))