def inorder(node):
    if node is not None:
      
        inorder(node.left)
      
        print(node.value)
  
        inorder(node.right)

