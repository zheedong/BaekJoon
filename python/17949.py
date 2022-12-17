crypto = input()
n = int(input())
crypto_type = input().split()

type_byte_dict = {"char" : 1, "int" : 4, "long_long" : 8}

def divide_crypto(crypto, crypto_type):
    idx = 0
    ret = []
    for cur_type in crypto_type:
        ret.append(crypto[idx : idx + 2 * type_byte_dict[cur_type]])
        idx += 2 * type_byte_dict[cur_type]
    return ret

ret = []
for hex in divide_crypto(crypto, crypto_type):
    ret.append(int(hex, 16))

print(*ret)