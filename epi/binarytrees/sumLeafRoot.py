class BinaryNode:
    def __init__(self,val,left,right):
        self.val = val
        self.left = left
        self.right = right    

def sumLeafToRoot(root):
    binaries = []
    def f(root, st):
        if root is None:
            return
        if root.left == None and root.right == None: 
            binaries.append(str(st))
            return
        f(root.left, st+root.val)
        f(root.right, st+root.val)
    f(root, "")
    return binaries


left = BinaryNode(
    "0",
    BinaryNode(
        "0",
        BinaryNode("0",None,None),
        BinaryNode("1",None,None)
        ),
    BinaryNode(
        "1",
        None,
        BinaryNode(
            "1",
            BinaryNode("0",None,None),
            None
        )
    )
)
right = BinaryNode(
    "1",
    BinaryNode(
        "0",
        None,
        BinaryNode(
            "0",
            BinaryNode(
                "1",
                None,
                BinaryNode("1",None,None)
            ),
            BinaryNode("0", None,None)
        )
    ),
    BinaryNode(
        "0",
        None,
        BinaryNode("0",None,None)
    )
)



root = BinaryNode("1",left,right)

print(sumLeafToRoot(root))

def sum_root_to_leaf(tree, partial_path_sum=0):
    if not tree:
        return 0
    partial_path_sum = partial_path_sum * 2 + int(tree.val)
    if not tree.left and not tree.right:
        return partial_path_sum
    return (sum_root_to_leaf(tree.left, partial_path_sum) + sum_root_to_leaf(
        tree.right, partial_path_sum))
print(sum_root_to_leaf(root, 0))