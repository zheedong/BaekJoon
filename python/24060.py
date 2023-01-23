n, k = map(int, input().split())
lst = list(map(int, input().split()))
flag = False
k_cnt = 1

tmp = [None for _ in range(len(lst))]

def merge(lst, p, q, r):
    global k_cnt
    global flag
    global tmp
    i = p
    j = q + 1
    t = 0
    while i <= q and j <= r:
        if lst[i] <= lst[j]:
            tmp[t] = lst[i]
            t += 1
            i += 1
        else:
            tmp[t] = lst[j]
            t += 1
            j += 1
    while i <= q:
        tmp[t] = lst[i]
        t += 1
        i += 1
    while j <= r:
        tmp[t] = lst[j]
        t += 1
        j += 1
    i = p
    t = 0
    while i <= r:
        lst[i] = tmp[t]
        if k_cnt == k:
            flag = True
            print(tmp[t])
        k_cnt += 1
        i += 1
        t += 1
        if flag:
            return

def merge_sort(lst, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(lst, p, q)
        merge_sort(lst, q + 1, r)
        merge(lst, p, q ,r)

merge_sort(lst, 0, n- 1)
if not flag:
    print(-1)