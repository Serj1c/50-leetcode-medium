class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(self, root: TreeNode) -> bool:
    def helper(root, lo, hi):
        if not root:
            return True
        if not lo < root.val < hi:
            return False 
        left = helper(root.left, lo, root.val)
        right = helper(root.right, root.val, hi)
        return left and right
    return helper(root, float('-inf'), float('inf'))