def postorder(node):
    if node is not None:
       
        postorder(node.left)
        
        postorder(node.right)
        
        print(node.value)

