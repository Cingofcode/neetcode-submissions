class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            return max(height(node.left),height(node.right)) +1

        def check(node):
            if node is None:
                return True
            if abs(height(node.left)-height(node.right)) > 1 :
                return False
            
            return check(node.left) and check(node.right)
        
        return check(root)