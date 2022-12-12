# https://docs.google.com/presentation/d/1rxgSEDv-haybhHFNwuYpVUpuZFZ67Stn/edit#slide=id.p6

import sys
input = sys.stdin.readline

k, h, q = map(int, input().split())

def get_d(blue, k):
    d = 0
    while True:
        if blue % (k + 1) != 0:
            break
        else:
            d += 1
            blue //= k + 1
    return d

def get_white_num(blue, k, d):
    return blue // ((k + 1) ** (d + 1))

def get_parent_white(white, k):
    d, v = white
    return (d + 1, v // (k + 1))

def is_tree_root(white, h):
    return True if white == (h - 1, 0) else False

def get_parent_path(white, k, h):
    ret = [white]
    parent = white
    while not is_tree_root(parent, h):
        parent = get_parent_white(parent, k)
        ret.append(parent)
    return ret

def get_white(blue, k):
    d = get_d(blue, k)
    return (d, get_white_num(blue, k, d))

def lca(path_1, path_2):
    path_1 = list(reversed(path_1))
    path_2 = list(reversed(path_2))
    if len(path_1) < len(path_2):
        for idx, node in enumerate(path_1):
            if node != path_2[idx]:
                return path_2[idx - 1]
        else:
            return path_2[idx]
    else:
        for idx, node in enumerate(path_2):
            if node != path_1[idx]:
                return path_1[idx - 1]
        else:
            return path_1[idx]

def dist_btw_white(root, white_path):
    return len(white_path) - list(reversed(white_path)).index(root)

blue_max = (k + 1) ** h - 1

for _ in range(q):
    blue_1, blue_2 = map(int, input().split())
    if blue_1 > blue_max or blue_2 > blue_max:
        print(-1)
    elif blue_1 == blue_2:
        print(0)
    else:
        white_path_1 = get_parent_path(get_white(blue_1, k), k, h)
        white_path_2 = get_parent_path(get_white(blue_2, k), k, h)
        white_lca = lca(white_path_1, white_path_2)
        print(dist_btw_white(white_lca, white_path_1) + dist_btw_white(white_lca, white_path_2))