while(True):
    try:
        inp = input()
        a, b = inp.split()
        a = int(a)
        b = int(b)
        print(a+b)
    except EOFError:
        break