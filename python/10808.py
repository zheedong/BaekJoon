str = list(input())
for alphabet in range(ord('a'), ord('z')):
    print(str.count(chr(alphabet)), end=" ")
print()