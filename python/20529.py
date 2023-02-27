from itertools import combinations
from collections import Counter
import sys
input = sys.stdin.readline

def get_2_mbti_dist(str1, str2):
    dist = 0
    for i in range(4):
        if str1[i] != str2[i]:
            dist += 1
    return dist

def get_3_mbti_dist(str1, str2, str3):
    return get_2_mbti_dist(str1, str2) + get_2_mbti_dist(str2, str3) + get_2_mbti_dist(str1, str3)

t = int(input())
for _ in range(t):
    n = int(input())
    if n > 32:
        _ = input()
        print(0)
        continue
    mbti_lst = input().split()
    count = Counter(mbti_lst)
    if count.most_common(1) == 3:
        print(0)
    else:
        min_dist = int(1e9)
        for comb in combinations(mbti_lst, 3):
            min_dist = min(min_dist, get_3_mbti_dist(*comb))
        print(min_dist)
