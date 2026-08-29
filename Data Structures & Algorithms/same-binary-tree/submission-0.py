# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None and q != None or p != None and q == None:
            return False
        sumArr1 = []
        sumArr2 = []
        def generateArr(binaryTree, sumArray):
            if binaryTree == None:
                sumArray.append("null")
                return sumArray
            sumArray.append(str(binaryTree.val))
            generateArr(binaryTree.left, sumArray)
            generateArr(binaryTree.right, sumArray)
        generateArr(p, sumArr1)
        generateArr(q, sumArr2)
        print(sumArr1)
        print(sumArr2)
        if len(sumArr1) != len(sumArr2):
            return False
        for i in range(0, len(sumArr1)):
            if sumArr1[i] != sumArr2[i]:
                return False
        return True

        