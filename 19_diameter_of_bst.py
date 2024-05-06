class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(self, root: TreeNode) -> int:
    self.ans = 0
    def helper(root):
        if not root:
            return 0
            
        left = helper(root.left)
        right = helper(root.right)
        self.ans = max(self.ans, left+right)
        return 1 + max(left, right)
    helper(root)
    return self.ans