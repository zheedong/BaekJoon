t = int(input())

for i in range(0, t):
    bachu_dict = {}
    m, n, k = map(int, input().split())
    for j in range(0, k):
        inp = list(map(int, input().split()))
        inp_tup = (inp[0], inp[1])
        bachu_dict[inp_tup] = j

    for l in bachu_dict:
        m, n = l
        if (m-1, n) in bachu_dict:
            bachu_dict[(m-1), n] = bachu_dict[(m, n)]
        elif (m+1, n) in bachu_dict:
            bachu_dict[(m+1, n)] = bachu_dict[(m, n)]
        elif (m, n-1) in bachu_dict:
            bachu_dict[(m, n-1)] = bachu_dict[(m, n)]
        elif (m, n+1) in bachu_dict:
            bachu_dict[(m, n+1)] = bachu_dict[(m, n)]
    print(len(list(set(bachu_dict.values()))))   