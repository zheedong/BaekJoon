def alphabet_to_num(alphabet):
    return ord(alphabet) - 96

def string_to_num_list(str):
    ret_arr = []
    for i in range(len(str)):
        ret_arr.append(alphabet_to_num(str[i]))
    return ret_arr

def hash_func(num_list):
    ret = 0
    for i in range(0, len(num_list)):
        ret += (num_list[i] * (31 ** i))
    return ret % 1234567891    # 마지막에 mod를 하는게 조금 더 빠르다. (+50점)

l = int(input())
inp_str = input()
print(hash_func(string_to_num_list(inp_str)))