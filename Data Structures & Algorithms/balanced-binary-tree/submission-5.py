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
        #leftSubTree = []
        #rightSubTree = []
        valid = True
        def findDiff(curNode: Optional[TreeNode], curSum: int, side: str) -> int:
            nonlocal valid
            if curNode == None:
                return curSum
            print(f"Corresponding value: {curNode.val}")
            print(f"CurSum Value: {curSum}")
            curSum += 1
            print(f"New CurSum Value: {curSum}")
            leftSide = findDiff(curNode.left, curSum, side)
            rightSide = findDiff(curNode.right, curSum, side)
            diff = abs(leftSide - rightSide)
            print(f"Difference: {diff}")
            if abs(leftSide - rightSide) > 1:
                print("Not a valid tree!")
                valid = False
            """
            if side == "left":
                leftSubTree.append(leftSide)
                leftSubTree.append(rightSide)
            else:
                rightSubTree.append(leftSide)
                rightSubTree.append(rightSide)
            """
            #print(f"Backtracking left side: {leftSide}")
            #print(f"Backtracking right side: {rightSide}")
            return max(leftSide, rightSide)
        print("Going to left subtree")
        leftSub = findDiff(root.left, 0, "left")
        print(f"value of valid: {valid}")
        if valid == False:
            return False
        #print(leftSubTree)
        """
        for i in range(0, len(leftSubTree)-1):
            if abs(leftSubTree[i] - leftSubTree[i+1]) > 1:
                return False
        """
        rightSub = findDiff(root.right, 0, "right")
        if valid == False:
            return False
        #print(rightSubTree)
        """
        for i in range(0, len(rightSubTree)-1):
            if abs(rightSubTree[i] - rightSubTree[i+1]) > 1:
                return False
        """
        #print(f"Max height for left side: {leftSub}")
        #print(f"Max height for right side: {rightSub}")
        return abs(leftSub - rightSub) <= 1