def count_odd_char(char_count):
    cnt = 0
    for char in char_count.keys():
        cnt += 1 if char_count[char] % 2 == 1 else 0
    return cnt

def get_half(char_count):
    ret = []
    for char in char_count.keys():
        ret += [char] * (char_count[char] // 2)
    return ret

def get_odd_char(char_count):
    for char in char_count.keys():
        if char_count[char] % 2 == 1:
            return char

def sol():
    inp = list(input())
    char_count = dict([])
    for char in sorted(list(set(inp))):
        char_count[char] = inp.count(char)

    odd_cnt = count_odd_char(char_count)
    if odd_cnt > 1:
        return "I'm Sorry Hansoo"
    elif odd_cnt == 1:
        half = get_half(char_count)
        return ("").join(half + [get_odd_char(char_count)] + list(reversed(half)))
    else:
        half = get_half(char_count)
        return ("").join(half + list(reversed(half)))
    
print(sol())