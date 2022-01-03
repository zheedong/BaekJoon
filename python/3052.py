inp_list = []

for _ in range(10):
    inp_list.append(int(input()))
    
mod_list = set(map(lambda x : x % 42, inp_list))
print(len(mod_list))