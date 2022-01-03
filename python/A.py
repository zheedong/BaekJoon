t = int(input())
for _ in range(t):
    x_list = [None] + list(map(int, input().split()))

    x_list[9] += x_list[6]
    x_list[6] = 0

    desirable_num = ''

    for number in range(9, 0, -1):
        for i in range(x_list[number]):
            desirable_num += str(number)

    def get_reverse(num_list):
        if len(num_list) == 1:
            return str(num_list[0])
        elif len(num_list) == 2:
            return str(num_list[0]) + str(num_list[1])
        else:
            return str(num_list[0]) + get_reverse(num_list[2:]) + str(num_list[1])

    res = get_reverse(desirable_num)
    for i in range(len(res)):
        print(res[i], end = " ")