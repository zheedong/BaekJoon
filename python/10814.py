n = int(input())

member_list = []

for i in range(0, n):
    age, name = input().split()
    age = int(age)
    member_list.append((age, name))
    
    
sorted_member = sorted(member_list, key = lambda x : x[0])

for i in range(0, n):
    age, name = sorted_member[i]
    print(str(age) + " " + name)