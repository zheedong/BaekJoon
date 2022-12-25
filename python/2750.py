n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))
lst.sort()
for num in lst:
    print(num) 