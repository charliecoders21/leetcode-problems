from TreeNode import TreeNode
def morris_inorder(root):
    """
    Perform Morris inorder traversal and return the list of node values.
    Time: O(n), Space: O(1) (excluding output list).
    """
    result = []
    curr = root

    while curr:
        if curr.left is None:
            # No left child: visit current and go right
            result.append(curr.val)
            curr = curr.right
        else:
            # Find inorder predecessor: rightmost in left subtree
            pred = curr.left
            while pred.right and pred.right is not curr:
                pred = pred.right

            if pred.right is None:
                # Make a temporary thread back to curr, then go left
                pred.right = curr
                curr = curr.left
            else:
                # Thread exists: remove it, visit curr, and go right
                pred.right = None
                result.append(curr.val)
                curr = curr.right

    return result

# Build a sample tree:
#       4
#     /   \
#    2     6
#   / \   / \
#  1  3  5  7

root = TreeNode(4,
    TreeNode(2, TreeNode(1), TreeNode(3)),
    TreeNode(6, TreeNode(5), TreeNode(7))
)

print(morris_inorder(root))         # Output: [1, 2, 3, 4, 5, 6, 7]
#print(list(morris_inorder_iter(root)))  # Output: [1, 2, 3, 4, 5, 6, 7]