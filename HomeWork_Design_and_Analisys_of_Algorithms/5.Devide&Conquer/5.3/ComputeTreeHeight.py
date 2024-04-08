# 3.Can you compute the height of a binary tree with the same asymptotic ef-
# ﬁciency as the section’s divide-and-conquer algorithm but without using a
# stack explicitly or implicitly? Of course, you may use a different algorithm
# altogether.



# Create tree
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

add_20_nodes(root)




# SOLUTION
# SOLUTION

def HeightOfTree(root):
    if root is None:
        return -1
    return max(HeightOfTree(root.left),HeightOfTree(root.right)) + 1

    
print("tree height is :",HeightOfTree(root))

    
