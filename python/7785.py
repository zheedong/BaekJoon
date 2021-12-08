import sys
n = int(input())

member_set = set() 

for i in range(0, n):
    name, in_out = sys.stdin.readline().strip().split()
    if in_out == "enter":
        member_set.add(name)
    elif in_out == "leave":
        member_set.remove(name)

sorted_list = sorted(member_set, reverse=True)

for out_name in sorted_list:
    print(out_name)