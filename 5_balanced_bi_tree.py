class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: TreeNode) -> bool:
    def helper(root):
        if not root:
            return True, 0
        
        l_is_b, lh = helper(root.left)
        r_is_b, rh = helper(root.right)

        if not l_is_b or not r_is_b:
            return False, -1
        
        return abs(lh-rh) < 2, 1 + max(lh, rh)
    
    return helper(root)[0]