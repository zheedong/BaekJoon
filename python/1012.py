# Graph Search
from collections import deque

def get_near_coordi(coordi):
    x, y = coordi
    return [(x-1, y+1), (x-1, y-1), (x+1, y+1), (x+1, y-1)]

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    jirungi_set = []        # Set of Position of Jirungi
    for _ in range(k):
        i, j = map(int, input().split())    
        jirungi_set.append((i, j))
        
    searched_node = set([])
    search_queue = deque(jirungi_set)
    ret_counter = 0        # TODO
    
    while search_queue:
        queue_pop = search_queue.pop()
        if queue_pop in searched_node:
            continue
        elif queue_pop in jirungi_set:
            searched_node.add(queue_pop)
            for node in get_near_coordi(queue_pop):
                search_queue.append(node)
            
    print(ret_counter)
            