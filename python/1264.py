while(True):
    inp = list(input().lower())
    if inp == ["#"]:
        break
    count = 0
    for char in inp:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            count += 1
    print(count)