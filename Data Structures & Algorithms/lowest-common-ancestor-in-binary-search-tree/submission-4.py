# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findCommonAncestor(curNode: TreeNode) -> TreeNode:
            if curNode.val == p.val or curNode.val == q.val:
                    return curNode
            if curNode.left and curNode.right:
                if curNode.left.val == p.val and curNode.right.val == q.val:
                    return curNode
                elif curNode.left.val == q.val and curNode.right.val == p.val:
                    return curNode
                elif p.val < curNode.val and q.val > curNode.val:
                    return curNode
                elif q.val < curNode.val and p.val > curNode.val:
                    return curNode
                elif p.val < curNode.val and q.val < curNode.val or p.val > curNode.val and q.val < curNode.val:
                    return findCommonAncestor(curNode.left)
                elif p.val > curNode.val and q.val > curNode.val:
                    return findCommonAncestor(curNode.right)
        return findCommonAncestor(root)
        