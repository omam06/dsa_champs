def count_leaves(root):
    if root is None:
        return 0
    if root[1] is None and root[2] is None:
        return 1
    
    return count_leaves(root[1]) + count_leaves(root[2])

tree1 = [8,
         [3, [1, None, None], [6, None, None]],
         [10, None, [14, None, None]]]

tree2 = [10,
         [5, [3, None, None], [7, None, None]],
         [15, None, None]]
print(count_leaves(tree1))
print(count_leaves(tree2))