# 3.Can you compute the height of a binary tree with the same asymptotic ef-
# ﬁciency as the section’s divide-and-conquer algorithm but without using a
# stack explicitly or implicitly? Of course, you may use a different algorithm
# altogether.


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

# Create a function to add 20 nodes to the binary tree
def add_20_nodes(tree):
    for i in range(1, 21):
        tree.add_node(i)

# Create the root node
root = TreeNode(10)

# Add 20 nodes to the binary tree
add_20_nodes(root)

