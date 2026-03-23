import sys
input = sys.stdin.readline

total_participants_N = int(input())
count_per_size = list(map(int, input().split(" ")))
assert total_participants_N == sum(count_per_size)
T, P = list(map(int, input().split(" ")))

def get_how_many_bundle(count):
    return ((count - 1) // T) + 1

print(sum(list(map(get_how_many_bundle, count_per_size))))
print(total_participants_N // P, total_participants_N % P)
