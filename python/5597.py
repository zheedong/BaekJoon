student_lst = [False for _ in range(31)]
student_lst[0] = None

for _ in range(28):
    cur_stu = int(input())
    student_lst[cur_stu] = True

for stu, is_sub in enumerate(student_lst):
    if is_sub == None:
        continue
    elif is_sub == False:
        print(stu)