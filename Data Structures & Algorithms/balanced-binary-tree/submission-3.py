# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        leftSubTree = []
        rightSubTree = []
        def findDiff(curNode: Optional[TreeNode], curSum: int, side: str) -> int:
            if curNode == None:
                return curSum
            print(f"Corresponding value: {curNode.val}")
            print(f"CurSum Value: {curSum}")
            curSum += 1
            print(f"New CurSum Value: {curSum}")
            leftSide = findDiff(curNode.left, curSum, side)
            rightSide = findDiff(curNode.right, curSum, side)
            if side == "left":
                leftSubTree.append(leftSide)
                leftSubTree.append(rightSide)
            else:
                rightSubTree.append(leftSide)
                rightSubTree.append(rightSide)
            print(f"Backtracking left side: {leftSide}")
            print(f"Backtracking right side: {rightSide}")
            return max(leftSide, rightSide)
        leftSub = findDiff(root.left, 0, "left")
        print(leftSubTree)
        for i in range(0, len(leftSubTree)-1):
            if abs(leftSubTree[i] - leftSubTree[i+1]) > 1:
                return False
        rightSub = findDiff(root.right, 0, "right")
        print(rightSubTree)
        for i in range(0, len(rightSubTree)-1):
            if abs(rightSubTree[i] - rightSubTree[i+1]) > 1:
                return False
        print(f"Max height for left side: {leftSub}")
        print(f"Max height for right side: {rightSub}")
        return abs(leftSub - rightSub) <= 1