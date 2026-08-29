# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def findAllNodes(curNode):
            if curNode == None:
                return []
            curList = []
            curList.extend(findAllNodes(curNode.left))
            curList.append(curNode.val)
            curList.extend(findAllNodes(curNode.right))
            return curList
        getList = findAllNodes(root)
        curEle = -1
        for i in range(0, k):
            curEle = getList[i]
        return curEle