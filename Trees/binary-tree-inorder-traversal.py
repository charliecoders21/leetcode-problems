from typing import Optional,List
from TreeNode import TreeNode


class Solution:
    #Inorder Traversal (Left → Root → Right)
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def Inorder(root):
            if not root:
                return
            Inorder(root.left)
            res.append(root.val)
            Inorder(root.right)
        Inorder(root)
        return res