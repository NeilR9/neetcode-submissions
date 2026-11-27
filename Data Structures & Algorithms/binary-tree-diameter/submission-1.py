# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    diameter = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        height = self.treeTraversalHelper(root)
        return max(self.diameter, height-1)
    
    def treeTraversalHelper(self, root):
        if root is None:
            return 0
        leftHeight = self.treeTraversalHelper(root.left)
        rightHeight = self.treeTraversalHelper(root.right)
        self.diameter = max(self.diameter, leftHeight + rightHeight)
        return max(leftHeight, rightHeight) + 1

        
