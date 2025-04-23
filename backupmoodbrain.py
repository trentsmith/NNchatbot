# Python program to find the node with minimum value in bst
 
# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
""" Give a binary search tree and a number,
inserts a new node with the given number in
the correct place in the tree. Returns the new
root pointer which the caller should then use
(the standard trick to avoid using reference
parameters). """
class moodTree:
  root = Node(0)
  def insert(node, data):
  
      # 1. If the tree is empty, return a new,
      # single node
      if node is None:
          return (Node(data))
  
      else:
          # 2. Otherwise, recur down the tree
          if data <= node.data:
            node.left=Node(data)
          elif data>=node.data:
            node.right =Node(data)
  
          # Return the (unchanged) node pointer
          return node
  
  """ Given a non-empty binary search tree, 
  return the minimum data value found in that
  tree. Note that the entire tree does not need
  to be searched. """
  def minValue(node,value):
      current = node
  
      # loop down to find the lefmost leaf
      while(current.left is not None):
          if(value <current.data):
            current = current.left
          elif(value >current.data):
            current = current.right
      return current.data
 
# Driver program


happiness = moodTree()
happiness.root = Node(0)
happiness.root = happiness.insert(happiness.root,4)
happiness.insert(happiness.root,2)
happiness.insert(happiness.root,1)
happiness.insert(happiness.root,3)
happiness.insert(happiness.root,6)
happiness.insert(happiness.root,5)
print(happiness.minValue(happiness.root,5))
 
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)