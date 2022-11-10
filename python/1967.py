import sys
input = sys.stdin.readline

node_num = int(input().rstrip())

adj_dist = [[None] for _ in range(node_num + 1)]

for _ in range(node_num - 1):
    from_node, to_node, weight = map(int, input().split())
    adj_dist[from_node].append((to_node, weight))
'''
tc1_node_num = 12
tc1 = [[None],
       [None, (2, 3), (3, 2)],
       [None, (4, 5)],
       [None, (5, 11), (6, 9)],
       [None, (7, 1), (8, 7)],
       [None, (9, 15), (10, 4)],
       [None, (11, 6), (12, 10)],
       [None],
       [None],
       [None],
       [None],
       [None],
       [None]]

tc2_node_num = 5
tc2 = [[None],
       [None, (2, 3), (3, 4), (4, 5), (5, 6)],
       [None],
       [None],
       [None],
       [None]] 

node_num = tc2_node_num
adj_dist = tc2
'''

def get_two_longest(node):
    ret = sorted(adj_dist[node][1:], key = lambda x : x[1], reverse=True)
    if len(ret) >= 2:
        ret = ret[0:2]
    elif len(ret) == 1:
        ret += [(None, 0)]
    elif len(ret) == 0:
        ret += [(None, 0), (None, 0)]
    return ret

global MAX_VALUE
MAX_VALUE = 0

def solution(root):
    '''
    PSUDO
    MAX = -1
    left, right
    ll, lr = solution(left)
    rl, rr = solution(right)
    max(MAX, ll + lr, max(ll, lr) + left_w + right_w + max(rl, rr), rl + rr)
    return [max(ll, lr) + left_w, right_w + max(rl, rr)]
    '''
    global MAX_VALUE
    (left, left_w), (right, right_w) = get_two_longest(root)
    if left == None and right == None:
        return [0, 0]
    elif right == None:
        ll, lr = solution(left)

        left_half = max(ll, lr) + left_w

        MAX_VALUE = max(MAX_VALUE, ll + lr, left_half)
        return [left_half, 0]
    else:
        ll, lr = solution(left)
        rl, rr = solution(right)

        left_half = max(ll, lr) + left_w
        right_half = right_w + max(rl, rr)

        MAX_VALUE = max(MAX_VALUE, ll + lr, left_half + right_half, rl + rr)
        return [left_half, right_half]

solution(1)
print(MAX_VALUE)