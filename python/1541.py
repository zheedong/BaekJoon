inp_str = input()

inp_format = inp_str.replace("+", " + ").replace("-", " - ").split()
# 기호들 좌우로 공백을 넣어주고, split 한다

ret = 0
minus_flag = False        # 한 번 -가 나오면 반드시 빼 줄 수 있다.

for i in range(0, len(inp_format), 2):
    value = inp_format[i]
    if minus_flag:
        ret -= int(value)
    else:
        ret += int(value)
        
    if not len(inp_format[i:]) == 1:
        if inp_format[i + 1] == '-':
            minus_flag = True

print(ret)