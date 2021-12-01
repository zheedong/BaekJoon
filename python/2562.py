inpArr = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 9):
    inpArr[i] = input()
inpArr = list(map(int, inpArr))

maxVal = max(inpArr)
maxIndex = inpArr.index(maxVal)

print(maxVal)
print(maxIndex + 1)
