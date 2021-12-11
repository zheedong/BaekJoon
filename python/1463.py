count_dict = dict([])

# n이 1인 경우 연산을 할 필요가 없다
count_dict[1] = 0  

n = int(input())

# 실패했던 이유 : Recursion을 사용해서 Stack을 과도하게 사용했다. 결국 전수 조사라서 Memory에 n개의 int가 저장되는건 피할 수 없다.
for i in range(2, n + 1):
    count_dict[i] = count_dict[i - 1] + 1
    if i % 3 == 0:
        count_dict[i] = min(count_dict[i], count_dict[int(i // 3)] + 1)
    if i % 2 == 0:
        count_dict[i] = min(count_dict[i], count_dict[int(i // 2)] + 1)

print(count_dict[n])