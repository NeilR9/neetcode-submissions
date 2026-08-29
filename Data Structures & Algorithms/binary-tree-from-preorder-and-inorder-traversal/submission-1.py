# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    preOrderList = []
    def treeHelper(self, nodes: List[int]) -> Optional[TreeNode]:
        if len(nodes) == 0:
            return None
        rootNodeEle = self.preOrderList[0]
        rootIndex = nodes.index(rootNodeEle)
        print(f"Root element: {rootNodeEle}")
        root = TreeNode(rootNodeEle)
        self.preOrderList = self.preOrderList[1:]
        print(f"Length of  left children: {len(nodes[0: rootIndex])}")
        root.left = self.treeHelper(nodes[0:rootIndex])
        print(f"Length of right children: {len(nodes[rootIndex:])}")
        root.right = self.treeHelper(nodes[rootIndex + 1:])
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preOrderList = preorder
        rootval = preorder[0]
        root = TreeNode()
        root.val = rootval
        root.left = None
        root.right = None
        self.preOrderList = self.preOrderList[1:]
        rootIndex = inorder.index(rootval)
        root.left = self.treeHelper(inorder[0:rootIndex])
        root.right = self.treeHelper(inorder[rootIndex + 1:])
        return root
