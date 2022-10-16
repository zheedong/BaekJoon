# Dynamic Programming... 인데 DP로 안 풀리네?
n = int(input())
inp_triangle = []
for _ in range(n):
    inp_triangle.append(list(map(int, input().split())))

tc1 = [[7],
       [3, 8],
       [8, 1, 0],
       [2, 7, 4, 4],
       [4, 5, 2, 6, 5]]

def div_2_triangle(triangle):
    tri1 = None 
    tri2 = None 
    for row in triangle[1:]:
        if tri1 == None:
            tri1 = []
            tri2 = []
        tri1.append(row[:-1])
        tri2.append(row[1:])
    return tri1, tri2

# ---- Top - down approach ----
# Naive recursion. TOO SLOW
def naive_rec(triangle):
    triangle_top = triangle[0][0]
    sub_tri_1, sub_tri_2 = div_2_triangle(triangle)
    if sub_tri_1 == None:
        return triangle_top
    else:
        return triangle_top + max(naive_rec(sub_tri_1), naive_rec(sub_tri_2))

# Dynamic Programming
# triangle을 받으면 최대 값을 출력
triangle_max_sum = dict([])

# list는 unhashable 하기 때문에 dict에 들어갈 수 없다. tuple로 바꿔주는 작업.
# 아마 메모리 초과의 이유 중 하나.
def double_list_to_tup(d_lst):
    return tuple(map(tuple, d_lst))

def dp_solution(triangle):
    triangle_tup = double_list_to_tup(triangle)
    try:
        # 이미 알고 있으면 return
        return triangle_max_sum[triangle_tup]
    except:
        triangle_top = triangle[0][0]
        sub_tri_1, sub_tri_2 = div_2_triangle(triangle)
        if sub_tri_1 == None:
            # triangle이 더이상 나눠지지 않는 1개 짜리인 경우. Base Case.
            triangle_max_sum[triangle_tup] = triangle_top
        else:
            triangle_max_sum[triangle_tup] = triangle_top + max(dp_solution(sub_tri_1), dp_solution(sub_tri_2))
        return triangle_max_sum[triangle_tup]

# DP로 풀면 풀릴 줄 알았는데... 메모리 초과가 나옴. 그래서 다른 접근 시도. DP 문제 맞긴 한데...
# 삼각형을 dict에 저장하는 방식에서 문제가 생기나? 했는데 naive recursion도 안 됨. div_2_triangle에 문제가 있나?

# ---- Bottom - up approach ----
def triangle_shrink(triangle):
    triangle_size = len(triangle)
    # Base Case. 크기 1인 삼각형은 그냥 값만 리턴.
    if triangle_size == 1:
        return triangle[0][0]
    # 아니라면, 자기 밑에 두 값 중 더 큰 값을 합쳐서 더해나감.
    base_row = triangle[-1]
    for idx, _ in enumerate(triangle[-2]):
        triangle[-2][idx] += max(base_row[idx], base_row[idx + 1])
    # 축소된 삼각형만 대상으로 다시 함수 실행.
    return triangle_shrink(triangle[:-1])

print(triangle_shrink(inp_triangle))