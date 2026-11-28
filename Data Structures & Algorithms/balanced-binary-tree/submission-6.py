# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    balanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height = self.isBalancedHelper(root)
        return self.balanced

    def isBalancedHelper(self, root):
        if root is None:
            return 0
        leftHeight = self.isBalancedHelper(root.left)
        rightHeight = self.isBalancedHelper(root.right)
        if (abs(leftHeight - rightHeight) > 1):
            self.balanced = False
        return max(leftHeight, rightHeight) + 1

    
        