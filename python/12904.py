s = list(input())
t = list(input())

while len(t) != len(s):
    if t[-1] == 'B':
        t = list(reversed(t[:-1]))
    else:
        t = t[:-1]

if t == s:
    print(1)
else:
    print(0)
