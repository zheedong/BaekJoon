n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

pos = [0] * (n + 1)
for i in range(n):
    pos[in_order[i]] = i

ret = []

# https://8iggy.tistory.com/112

def in_post_to_pre(in_l, in_r, post_l, post_r):
    if in_l > in_r or post_l > post_r:
        return
    root = post_order[post_r]
    mid = pos[root]
    left = mid - in_l
    right = in_r - mid
    ret.append(root)
    in_post_to_pre(in_l, in_l + left - 1, post_l, post_l + left - 1)
    in_post_to_pre(in_r - right + 1, in_r, post_r - right, post_r - 1)

in_post_to_pre(0, n - 1, 0, n - 1)
print(*ret)