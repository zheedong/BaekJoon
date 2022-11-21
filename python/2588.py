num_1 = int(input())
str_2 = input()

for num in reversed(str_2):
    print(num_1 * int(num))
print(num_1 * int(str_2))