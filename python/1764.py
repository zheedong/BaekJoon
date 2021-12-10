n, m = map(int, input().split())

no_listen_set = set()
no_see_set = set()

for _ in range(0, n):
    no_listen_set.add(input())

for _ in range(0, m):
    no_see_set.add(input())
    
no_listen_see_set = sorted(no_see_set & no_listen_set)

set_len = len(no_listen_see_set)
print(set_len)

for i in range(0, set_len):
    print(no_listen_see_set[i])