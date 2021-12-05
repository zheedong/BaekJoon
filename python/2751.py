# PyPy3로 실행하면 풀림!
# N이 크기 때문에 문제가 발생한다.
n = int(input())

inp_set = set()

for i in range(0, n):
    inp_set.add(int(input()))

sorted_set = sorted(inp_set)
    
for i in sorted_set:
    print(i)