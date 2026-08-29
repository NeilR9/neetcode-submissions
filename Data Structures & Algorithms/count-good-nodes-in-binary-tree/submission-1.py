# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def findGoodNodes(root, maxVal):
            if root == None:
                return 0
            curSum = 0
            print(root.val)
            #print(f"Max Val: {maxVal}")
            if root.val >= maxVal:
                curSum += 1
                maxVal = root.val
            return curSum + findGoodNodes(root.left, maxVal) + findGoodNodes(root.right, maxVal)
        return findGoodNodes(root, root.val)
        