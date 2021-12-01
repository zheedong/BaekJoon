x, y, w, h = input().split()

x = int(x)
y = int(y)
w = int(w)
h = int(h)

bigger_x = x
bigger_y = y

if w-x < x:
   bigger_x = w-x
if h-y < y:
    bigger_y = h-y
    
if bigger_x > bigger_y:
    print(bigger_y)
else:
    print(bigger_x)