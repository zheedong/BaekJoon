import sys
input = sys.stdin.readline

G = int(input())
P = int(input())

gates = [None for _ in range(G)]
max_plane = -int(1e9)

def sol(plane_idx):
    global max_plane
    if plane_idx > G - 1:
        max_plane = max(max_plane, G - gates.count(None))
        return
    g_i = g_i_lst[plane_idx]
    for idx, val in enumerate(gates[:g_i + 1]):
        if val == None:
            gates[idx] = plane_idx 
            sol(plane_idx + 1)
            gates[idx] = None
    else:
        max_plane = max(max_plane, G - gates.count(None))
        return

g_i_lst = []

for _ in range(P):
    g_i_lst.append(int(input()) - 1)

sol(0)
print(max_plane)