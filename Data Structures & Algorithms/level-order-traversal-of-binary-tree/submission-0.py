# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class NodeInfo:
    def __init__(self, curNode=None, level=0):
        self.curNode= curNode
        self.level=level
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        curQueue = deque()
        curList = []
        prevInfo = None
        firstList = []
        curQueue.append(NodeInfo(root, 0))
        while curQueue:
            #print(f"First List: {firstList}")
            curInfo = curQueue.popleft()
            getNode = curInfo.curNode
            if prevInfo and curInfo.level != prevInfo.level:
                curList.append(firstList)
                firstList = []
            firstList.append(getNode.val)
            if getNode.left:
                curQueue.append(NodeInfo(getNode.left, curInfo.level+1))
            if getNode.right:
                curQueue.append(NodeInfo(getNode.right, curInfo.level+1))
            prevInfo = curInfo
        curList.append(firstList)
        return curList