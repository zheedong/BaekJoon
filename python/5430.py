import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    try:
        p = list(input().rstrip())
        n = int(input().rstrip())

        # Input의 길이가 0인 경우는 특별히 처리
        if n == 0:
            inp = input().rstrip()
            for command in p:
                if command == "D":
                    raise Exception
            print("[]")
        else:
            inp = list(map(int, input().rstrip()[1:-1].split(",")))

            # R 이 되었는지를 기록. 진짜로 뒤집으면 큰일난다. (취직을 못함)
            is_reversed = False
            left_idx = 0
            right_idx = n - 1

            for command in p:
                if command == "R":
                    is_reversed = not(is_reversed)
                elif command == "D":
                    if left_idx > right_idx:
                        raise Exception
                    # 뒤집어졌는지 여부에 따라 index를 바꾼다.
                    elif is_reversed:
                        right_idx -= 1
                    else:
                        left_idx += 1

            # index에 기반해 inp을 잘라냄
            inp = inp[left_idx:right_idx + 1]

            if is_reversed:
                inp.reverse()

            print("[", end="")
            print(*inp, sep=",", end="")
            print("]")
    except:
        print("error")