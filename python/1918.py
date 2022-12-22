from collections import deque

mid_fix = list(input())
post_fix = []

stack = deque([])
for cur_str in mid_fix:
    if cur_str == '(':
        stack.append(cur_str)
    elif cur_str ==')':
        while stack and stack[-1] != '(':
            post_fix.append(stack.pop())
        stack.pop()
    elif cur_str == '*' or cur_str == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            post_fix.append(stack.pop())
        stack.append(cur_str)
    elif cur_str == '+' or cur_str == '-':
        while stack and stack[-1] != '(':
            post_fix.append(stack.pop())
        stack.append(cur_str)
    else:
        post_fix.append(cur_str)

while stack:
    post_fix.append(stack.pop())

print("".join(post_fix))