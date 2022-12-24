t = int(input())

def vector_size(vec):
    x, y = vec
    return x ** 2 + y ** 2

for _ in range(t):
    init_x, init_y = map(int, input().split())
    vector = [(0, 0)]
    farest = ()
    for _ in range(3):
        x, y = map(int, input().split())
        vector.append((x - init_x, y - init_y))
    vector.sort(key=lambda x : vector_size(x))
    print(vector)
    x1, y1 = vector[1]
    x2, y2 = vector[2]
    x3, y3 = vector[3]
    if x1 == y2 and y1 == x2:
        if x1 + x2 == x3 and y1 + y2 == y3:
            if x1 * x2 - y1 * y2 == 0:
                print(1) 
                continue
    print(0)
    
    