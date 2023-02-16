import sys
input = sys.stdin.readline

n = int(input())
members = []

for member_idx in range(n):
	v, x = map(int, input().split())
	members.append((v, x))

total_resource = 0

members.sort(key=lambda x: -x[0])

for mem1 in range(n - 1):
    for mem2 in range(mem1 + 1, n):
        total_resource += abs(members[mem1][1] - members[mem2][1]) * members[mem1][0]

print(total_resource)
