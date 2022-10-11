n = int(input())

img_mat = []

for _ in range(n):
    img_mat.append(list(map(int, list(input()))))

def is_all_same(mat):
    flag = True
    init = mat[0][0]
    for row in mat:
        for val in row:
            flag = flag and (init == val)
    return flag

def mat_divided_4(mat):
    size_n = len(mat)
    half_size = size_n // 2
    ret = []
    for i in [0, half_size]:
        for j in [0, half_size]:
            ret.append([row[j:j+half_size] for row in mat[i:i+half_size]])
    return ret

def zip_img(img):
    if is_all_same(img):
        return img[0][0]
    else:
        divided_mat_list = mat_divided_4(img)
        ret_str = ""
        for divided_mat in divided_mat_list:
            ret_str += str(zip_img(divided_mat))
        return "(" + ret_str + ")"

print(zip_img(img_mat))