def check_friend(x, y):
    if set(x) == set(y):
        return True
    else:
        return False

def make_new_plus(int_str, i):
    int_str[i] += 1
    int_str[i + 1] -= 1
    return int_str

def make_new_minus(int_str, i):
    int_str[i] -= 1
    int_str[i + 1] += 1
    return int_str

def check_near_friend(x, y):
    for i in range(len(y) - 1):
        new_plus_y = make_new_plus(y, i)
        if check_friend(x, new_plus_y):
            return True
        else:
            make_new_minus(y, i)

        new_minus_y = make_new_minus(y, i)
        if check_friend(x, new_minus_y) and new_minus_y[0] != 0:
            return True
        else:
            make_new_plus(y, i)
    else:
        return False

for _ in range(3):
    x, y = map(int, input().split())
    x = list(map(int, list(str(x))))
    y = list(map(int, list(str(y))))

    if check_friend(x, y):
        print("friends")
    elif check_near_friend(x, y) or check_near_friend(y, x):
        print("almost friends")
    else:
        print("nothing")

