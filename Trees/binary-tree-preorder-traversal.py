from TreeNode import TreeNode
from typing import Optional,List

class Solution:
    #Preorder Traversal (Root → Left → Right)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def preorder(root):
            if not root:
                return
            res.append(root.val)
            preorder(root.left)
            
            preorder(root.right)
            
        preorder(root)
        return res