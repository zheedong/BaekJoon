import sys
input = sys.stdin.readline

n = int(input().rstrip())
num_list = list(map(int, input().split()))
palindrome_set = [[None for _ in range(n)] for _ in range(n)]


def check_palindrome(s, e):
    global palindrome_set
    new_check = []
    is_palindrome = None

    while True:
        new_check.append((s, e))
        if palindrome_set[s][e] is not None:
            is_palindrome = palindrome_set[s][e]
            break
        elif s >= e:
            is_palindrome = True
            break
        elif num_list[s] != num_list[e]:
            is_palindrome = False
            break
        else:
            s += 1
            e -= 1

    for x, y in new_check:
        palindrome_set[x][y] = is_palindrome

    return palindrome_set[s][e]

m = int(input().rstrip())
for _ in range(m):
    s, e = map(int, input().split())
    if check_palindrome(s - 1, e - 1):
        print(1)
    else:
        print(0)