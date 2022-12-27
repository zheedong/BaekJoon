import sys
input = sys.stdin.readline
sys.setrecursionlimit(15000)

def pre_to_post_order(pre_order, root, end):
    ret = []
    # If only has root
    if root > end:
        return []
    elif root == end:
        return [pre_order[root]]

    cur_root = pre_order[root]

    # Check left
    left = root + 1
    # Check right
    for right in range(end, root, -1):
        if pre_order[right] < cur_root:
            right += 1
            break
    
    if left == right:
        ret += pre_to_post_order(pre_order, left, end)
    else:
        ret += pre_to_post_order(pre_order, left, right - 1)
        ret += pre_to_post_order(pre_order, right, end)
    ret.append(cur_root)

    return ret

def sol():
    pre_order = []
    while True:
        try:
            pre_order.append(int(input().rstrip()))
        except:
            break
    for num in pre_to_post_order(pre_order, 0, len(pre_order) - 1):
        print(num)

sol()