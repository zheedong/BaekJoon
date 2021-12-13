'''
종류 n 개
종류 속 개수 [k, m, n, ...]
조합 (kC1 + kC0) * (mC1 + mC0) * ... - 1
'''

number_of_test_case = int(input())

for _ in range(number_of_test_case):
    n = int(input())

    type_name_dict = dict([])

    for _ in range(n):
        cloth_name, cloth_type = input().split()

        if cloth_type in type_name_dict:
            type_name_dict[cloth_type] = type_name_dict[cloth_type].union(set([cloth_name]))
        else:
            type_name_dict[cloth_type] = set([cloth_name])

    number_of_selection = 1

    for cloth_type_set in type_name_dict.values():
        number_of_type = len(cloth_type_set)
        number_of_selection *= (number_of_type + 1)

    print(number_of_selection - 1)