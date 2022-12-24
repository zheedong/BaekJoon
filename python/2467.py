from bisect import bisect_left

n = int(input())
solution_list = list(map(int, input().split()))

most_near_val = int(1e12)
most_near_sol_1 = None
most_near_sol_2 = None

for idx, solution in enumerate(solution_list):
    poss_idx = bisect_left(solution_list, -solution) - 1
    candidates = []

    if poss_idx > 0 and poss_idx != idx:
        candidates.append(solution_list[poss_idx])
    elif poss_idx - 1 > 0 and poss_idx - 1 != idx:
        candidates.append(solution_list[poss_idx - 1])

    if poss_idx + 1 < n and poss_idx + 1 != idx:
        candidates.append(solution_list[poss_idx + 1])

    for new_sol in candidates:
        if abs(solution + new_sol) < most_near_val:
            most_near_val = abs(solution + new_sol)
            most_near_sol_1 = solution
            most_near_sol_2 = new_sol

print(*sorted([most_near_sol_1, most_near_sol_2]))