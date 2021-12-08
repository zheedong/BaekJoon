n = int(input())
holding_cards = list(map(int, input().split()))

count_dict = {}

# O(n)
for card in holding_cards:
    count_dict[card] = 0
# O(n)
for card in holding_cards:
    count_dict[card] += 1

m = int(input())
check_cards = list(map(int, input().split()))

# O(m)
for card in check_cards:
    try:
        print(count_dict[card], end=" ")
    except:
        print(0, end=" ")