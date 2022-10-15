from itertools import combinations_with_replacement

n, m = map(int, input().split())

# 중복 선택이 가능하기 때문에 input으로 중복된 값이 들어 오는 것은 의미가 없다. set으로 정리.
inp_lst = sorted(list(set(map(int, input().split()))))

# 중복 순열인 줄 알았는데... 메모리 문제 발생
# 중복 조합 후 순서를 줄려 했는데 그럴 필요 없이 풀림.
for data in combinations_with_replacement(inp_lst, m):
    print(*data)