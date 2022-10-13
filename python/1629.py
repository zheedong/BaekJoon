a, b, c = map(int, input().split())

# b를 2진수로 변환, 앞에 1b는 떼고 str로 저장
b_bin = bin(b)[2:]

b_pow_sum = []

# b가 어떤 2의 거듭제곱 꼴들의 합으로 나타나는지 저장.
for idx, p in enumerate(b_bin[::-1]):
    if int(p) == 1:
        b_pow_sum.append(2 ** idx)

# a^b mod c 의 값들을 저장해 두는 dict
mod_dict = dict([])
mod_dict[1] = a % c 

# Dynamic Programming. a^b mod c (단, 어떤 자연수 k에 대해 b = 2^k) 을 계산한다.
def get_2_pow_mod(k_tup,mod_dict):
    a, b, c = k_tup
    try:
        return mod_dict[b]
    except:
        k = get_2_pow_mod((a, b // 2, c), mod_dict) 
        # DP를 위해 저장한다.
        mod_dict[b] = (k ** 2) % c
        return mod_dict[b]

# b보다 작은 2의 거듭제곱 꼴에 대해서 위 함수를 계산한다.
k = 1
while k <= b:
    get_2_pow_mod((a, k, c), mod_dict)
    k *= 2

# mod_dict와 b가 어떤 거듭제곱들로 이루어졌는지를 바탕으로 최종 결과 값을 계산한다.
res = 1
for i in b_pow_sum:
    res *= mod_dict[i]
print(res % c)