# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True 
        
        self.maxDiff = 0

        def getHeight(node):
            if not node: 
                return 0
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)

            self.maxDiff = max(self.maxDiff, abs(right_height-left_height))
            return 1 + max(left_height, right_height)
        
        getHeight(root)

        if self.maxDiff==1 or self.maxDiff==0: 
            return True
        else:
            return False

        