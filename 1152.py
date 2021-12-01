inp = input().strip()

if len(inp) == 0:
    print("0")
else:
    print(inp.count(" ") + 1)