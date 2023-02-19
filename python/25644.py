n = int(input())
price = list(map(int, input().split()))

max_price = price[-1]
ans = -int(1e9)

for idx in range(-1, -len(price)-1, -1):
    if price[idx] > max_price:
        max_price = price[idx]
    ans = max(ans, max_price - price[idx])
print(ans)

