arrLen = int(input())

inp = [0 for i in range(arrLen)]
inp = input().split()
inp = list(map(int, inp))

maxScore = max(inp)

sum = 0

for i in range(len(inp)):
    sum += inp[i]
ave = sum / arrLen

print(ave/maxScore * 100)
