class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.add_node(data)
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.add_node(data)

def add_20_nodes(tree):
    for i in range(1, 21):
        tree.add_node(i)

root = TreeNode(10)

# Add 20 nodes to the binary tree
add_20_nodes(root)


def findMaxLevelRecursively(root):
    if root is None:
        return 0
    left= findMaxLevelRecursively(root.left)  
    right = findMaxLevelRecursively(root.right)
    return  max(left,right) + 1



print("res: ",findMaxLevelRecursively(root))