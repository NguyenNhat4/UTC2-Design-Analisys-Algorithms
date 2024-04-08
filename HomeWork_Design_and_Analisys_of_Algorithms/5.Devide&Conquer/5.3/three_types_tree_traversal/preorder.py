def preorder(node):
    if node is not None:
       
        print(node.value)
      
        preorder(node.left)
    
        preorder(node.right)
