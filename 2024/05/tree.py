class Node:
   def __init__(self, data, customCompare = None):
      defaultCompareFn = lambda a, b : a - b
      self.left = None
      self.right = None
      self.data = data
      self.compare = customCompare if customCompare is not None else defaultCompareFn

# Insert Node
   def insert(self, data):   
      if self.data:
         if self.compare(data, self.data) < 0:
            if self.left is None:
               self.left = Node(data, self.compare)
            else:
               self.left.insert(data)
         elif self.compare(data, self.data) > 0:
            if self.right is None:
               self.right = Node(data, self.compare)
            else:
               self.right.insert(data)
      else:
         self.data = data

# Print the Tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()

# Inorder traversal
# Left -> Root -> Right
   def inorderTraversal(self, root):
      res = []
      if root:
         res = self.inorderTraversal(root.left)
         res.append(root.data)
         res = res + self.inorderTraversal(root.right)
      return res