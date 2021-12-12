# WHITE : 0
# BLUE : 1

def check_all_white(matrix):
    n_size = len(matrix[0])
    n_matrix = [[0 for col in range(n_size)] for row in range(n_size)]
    
    if n_matrix == matrix:
        return True
    else:
        return False
    
def check_all_blue(matrix):
    n_size = len(matrix[0])
    n_matrix = [[1 for col in range(n_size)] for row in range(n_size)]
    
    if n_matrix == matrix:
        return True
    else:
        return False
    
def add_four_tuple(tup1, tup2, tup3, tup4):
    a, b = tup1
    c, d = tup2
    e, f = tup3
    g, h = tup4
    return (a+c+e+g, b+d+f+h)

def divide_matrix(matrix):
    n_size = len(matrix[0])
    half_size = int(n_size / 2)
    
    upper_row = matrix[:half_size]
    lower_row = matrix[half_size:]
    
    mat_1 = list(map(lambda x : x[:half_size], upper_row))
    mat_2 = list(map(lambda x : x[:half_size], lower_row))
    mat_3 = list(map(lambda x : x[half_size:], upper_row))
    mat_4 = list(map(lambda x : x[half_size:], lower_row))
    return (mat_1, mat_2, mat_3, mat_4)
    

def get_count(matrix):
    if check_all_white(matrix):
        return (1, 0)
    elif check_all_blue(matrix):
        return (0, 1)
    else:
        mat1, mat2, mat3, mat4 = divide_matrix(matrix)
        return add_four_tuple(get_count(mat1), get_count(mat2), get_count(mat3), get_count(mat4))
    
n = int(input())

inp_matrix = [[0 for col in range(n)] for row in range(n)]

for row in range(n):
    inp_matrix[row] = list(map(int, input().split()))
    
for ret in get_count(inp_matrix):
    print(ret)