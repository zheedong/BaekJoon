n = int(input())

class Tree:
    left_node = None
    right_node = None
    
node_dict = dict([])

for i in range(n):
    root, left, right = input().split()
    node_dict[root] = Tree()
    node_dict[root].left_node = left
    node_dict[root].right_node = right
    
def prefix(root):
    left = node_dict[root].left_node
    right = node_dict[root].right_node
    if left == '.' and right == '.':
        return root
    elif left != '.' and right == '.':
        return root + prefix(left)
    elif left == '.' and right != '.':
        return root + prefix(right) 
    else:
        return root + prefix(left) + prefix(right)
    
def infix(root):
    left = node_dict[root].left_node
    right = node_dict[root].right_node
    if left == '.' and right == '.':
        return root
    elif left != '.' and right == '.':
        return infix(left) + root
    elif left == '.' and right != '.':
        return root + infix(right)
    else:
        return infix(left) + root + infix(right)
    
def postfix(root):
    left = node_dict[root].left_node
    right = node_dict[root].right_node
    if left == '.' and right == '.':
        return root
    elif left != '.' and right == '.':
        return postfix(left) + root
    elif left == '.' and right != '.':
        return postfix(right) + root
    else:
        return postfix(left) + postfix(right) + root
    
print(prefix('A'))
print(infix('A'))
print(postfix('A'))