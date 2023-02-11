while True:
    n = int(input())
    if n == 0:
        break

    charger_posn = []
    for _ in range(n):
        charger_posn.append(int(input()))
    charger_posn.sort()

    if 2 * (1422 - charger_posn[-1]) > 200:
        print("IMPOSSIBLE")
    else:
        for i in range(len(charger_posn) - 1):
            if charger_posn[i + 1] - charger_posn[i] > 200:
                print("IMPOSSIBLE")
                break
        else:
            print("POSSIBLE")
