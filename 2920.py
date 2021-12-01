inpArr = [0 for i in range(0, 8)]
inpArr = input().split()
inpArr = list(map(int, inpArr))

ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]

if inpArr == ascending:
    print("ascending")
elif inpArr == descending:
    print("descending")
else:
    print("mixed")