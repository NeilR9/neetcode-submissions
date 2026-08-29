# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class NodeInfo:
    def __init__(self, curNode=None, level=0):
        self.curNode = curNode
        self.level = level
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        curQueue = deque()
        curQueue.append(NodeInfo(root, 0))
        prevInfo = None
        curList = []
        while curQueue:
            curInfo = curQueue.popleft()
            getNode = curInfo.curNode
            if prevInfo != None and curInfo.level != prevInfo.level:
                curList.append(prevInfo.curNode.val)
            if getNode.left:
                curQueue.append(NodeInfo(getNode.left, curInfo.level + 1))
            if getNode.right:
                curQueue.append(NodeInfo(getNode.right, curInfo.level + 1))
            prevInfo = curInfo
        curList.append(prevInfo.curNode.val)
        return curList
            
