class countCall:
    count_zero = 0
    count_one = 0

def get_nth_fibonacci_number(countCall, n):
    if n == 0:
        countCall.count_zero += 1
        return 0
    elif n == 1:
        countCall.count_one += 1
        return 1
    else:
        return get_nth_fibonacci_number(countCall, n - 1) + get_nth_fibonacci_number(countCall, n - 2)

index = int(input())

for i in range(0, index):
    count = countCall()
    get_nth_fibonacci_number(count, int(input()))
    print(str(count.count_zero) + " " + str(count.count_one))