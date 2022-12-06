from collections import deque

n, k = map(int, input().split())

queue = deque([i for i in range(1, n + 1)])
dead_people = []

# queue implementation
while queue:
    # pop and push immediatly (just like circle queue)
    for _ in range(k - 1):
        pop = queue.popleft()
        queue.append(pop)
    # pop dead one and not push again
    dead_people.append(queue.popleft())

# FANCY trick to print
print("<", end="")
for x in dead_people[:-1]:
    print(x, end=", ")
print(f"{dead_people[-1]}>")