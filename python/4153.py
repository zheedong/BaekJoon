def check_perp(a, b, c):
    square_side_list = [a*a, b*b, c*c]
    sorted_list = sorted(square_side_list)
    if ((sorted_list[0] + sorted_list[1]) == sorted_list[2]):
        return("right")
    else:
        return("wrong")
    
while(True):
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    
    if(a == b == c == 0):
        break
    
    print(check_perp(a, b, c))