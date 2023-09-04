# NEETCODE Optimal Solution:
# The concept is to keep the root and swap it's children.
# So first, we check if the tree is present, else return None
# Then, write the swap function, such that it can be applied to subtrees- swap left and right children
# Now recursively swap left and right subtrees
# Return root

# THIS IS A DFS ALGORITHM

# Time Complexity = O(n) where n is number of nodes in the tree- we are traversing each node only once
# Space Complexity = O(h) where h is the height of the tree- maximim depth of the recursion tree generated

-----------------------------------------------------------------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root: 
            return None
        
        # swap left and right child
        temp = root.left
        root.left = root.right
        root.right = temp

        # apply the function to left and right children- RECURSION
        self.invertTree(root.left)
        self.invertTree(root.right)

        # return the tree
        return root

-----------------------------------------------------------------------------------------------------------------------
