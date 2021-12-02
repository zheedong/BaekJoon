test_case_1 = """
121
1231
12421
0
"""

while(True):
    inp_str = input()

    if int(inp_str) == 0:    # exit case = 0
        break
        
    reversed_inp_str = inp_str[::-1]
    if int(inp_str) == int(reversed_inp_str):
        print("yes")
    else:
        print("no")
    
