from collections import deque
import sys

# 1시간 40분 걸림 ㅋㅋ;;

n, m = map(int, input().split())        # 또!! n, m을 뒤집어서 받았다

tomato_map = []

def get_near_4(coordi):
    row, col = coordi
    return [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        
for _ in range(m):
    tomato_map.append(list(map(int, sys.stdin.readline().strip().split())))
    
not_ripped_tomato_set = set()
ripped_tomato_set = set()
empty_space_set = set()

search_queue = deque()

for row in range(len(tomato_map)):
    for col in range(len(tomato_map[row])):
        if tomato_map[row][col] == 1:
            ripped_tomato_set.add((row, col))
            search_queue.append((0, (row, col)))        # Add with depth (Initial value 0)
        elif tomato_map[row][col] == 0:
            not_ripped_tomato_set.add((row, col))
        elif tomato_map[row][col] == -1:
            empty_space_set.add((row, col))
    
valid_pos_set = ripped_tomato_set | not_ripped_tomato_set | empty_space_set

ret_count = -1

searched_pos = set()

while search_queue:
    depth, cul_pos = search_queue.popleft()
    
    # Check Already Visited
    if cul_pos in searched_pos:
        continue
        
    # Check break situation
    if cul_pos in empty_space_set:
        continue
    
    # Add to searched
    searched_pos.add(cul_pos)
    
    # If current is not in ripped_tomato_set => update 
    if cul_pos not in ripped_tomato_set:
        ripped_tomato_set.add(cul_pos)
        not_ripped_tomato_set.remove(cul_pos)
        
    # Get near 4 coordi
    near4 = get_near_4(cul_pos)
    for pos in near4:
        if pos in valid_pos_set:                         # Add search queue only valid coordi
            search_queue.append((depth + 1, pos))        # Increase depth 
    
if not_ripped_tomato_set:
    print(-1)
else:
    print(depth - 1)