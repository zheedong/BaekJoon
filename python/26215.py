import heapq

n = int(input())
nums = list(map(int, input().split()))
houses = []
for num in nums:
    heapq.heappush(houses, (-num, num))

def sol(houses):
    if len(houses) == 0:
        return 0
    elif len(houses) == 1:
        return houses[0][1]
    else:
        max1 = heapq.heappop(houses)[1]
        max2 = heapq.heappop(houses)[1]
        if max1 - max2 != 0:
            heapq.heappush(houses, (max2 - max1, max1 - max2))
        return max2 + sol(houses)

res = sol(houses)
print(-1 if res > 1440 else res)