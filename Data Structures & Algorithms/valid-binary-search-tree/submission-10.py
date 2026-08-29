# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validStackEle(value, curStack, operatorStack):
            #print(f"Curent value: {value}")
            for i in range(0, len(curStack)):
                #print(f"Stack value: {curStack[i]}")
                #print(f"Operator: {operatorStack[i]}")
                if operatorStack[i] == "<":
                    if value >= curStack[i]:
                        return False
                elif operatorStack[i] == ">":
                    #print(f"It should be greater than or equal to")
                    if value <= curStack[i]:
                        #print(f"Invalid value!")
                        return False
            return True 
        def determineTree(root, curStack, operatorStack):
            #print(f"Current value: {root.val}")
            #print(f"current stack: {curStack}")
            #print(f"operator stack: {operatorStack}")
            if root == None or root.left == None and root.right == None:
                return True
                #print("At least 1 child is with it!")
            if root.left:
                #print(f"Left value: {root.left.val}")
                if root.left != None and root.left.val >= root.val:
                    return False
                elif validStackEle(root.left.val, curStack, operatorStack) == False:
                    return False
            #print("Left node good!")
            if root.right:
                if root.right.val <= root.val:
                    return False
                elif validStackEle(root.right.val, curStack, operatorStack) == False:
                    return False
            curStack.append(root.val)
            leftCurStack = curStack.copy()
            rightCurStack = curStack.copy()
            #print(f"Adding Value {root.val}")
            #print(f"Length of stack: {curStack}")
            leftStack = []
            rightStack = []
            leftStack = leftStack + operatorStack
            rightStack = rightStack + operatorStack
            leftStack.append("<")
            rightStack.append(">")
            #print("Both child node are good!")
            if determineTree(root.left, leftCurStack, leftStack) and determineTree(root.right, rightCurStack, rightStack):
                return True
            else:
                return False
        return determineTree(root, [], [])


