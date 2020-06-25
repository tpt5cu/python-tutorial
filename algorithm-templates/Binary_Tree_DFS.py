




#Bottom Up
"""
go down left tree, vist right, hit root, then right, left. DIFFERENT THAN IN ORDER. IN ORDER GOES LEFT, NODE, RIGHT FOR ALL NODES

Please see and vote for my solutions for these similar problems.
250. Count Univalue Subtrees
508. Most Frequent Subtree Sum
543. Diameter of Binary Tree
1245. Tree Diameter
687. Longest Univalue Path
124. Binary Tree Maximum Path Sum
Max Path Sum in a Grid
298. Binary Tree Longest Consecutive Sequence
549. Binary Tree Longest Consecutive Sequence II

A path may or may not pass through the root.
All paths = {all paths passing through a node and its desendants | for each node in tree}.
Bottom-up DFS: from bottom to top,
find the longest path passing through a node and its descendants,
and updade the global longest path.


"""
#example

def diameterOfBinaryTree(self, root: TreeNode) -> int:
    def depth(root):
        if not root:
            return 0
        l_depth = depth(root.left)
        r_depth = depth(root.right)
        res[0] = max(res[0], l_depth + r_depth)
        return 1 + max(l_depth, r_depth)
    
    res = [0]
    depth(root)
    return res[0]




#TOP DOWN

"""
Like above but in reverse

Similair

129. Sum Root to Leaf Numbers
1022. Sum of Root To Leaf Binary Numbers
988. Smallest String Starting From Leaf
112. Path Sum
113. Path Sum II
437. Path Sum III
"""


#Example
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        paths = []
        def dfs(node, path):
            if not node.left and not node.right:
                paths.append(path+str(node.val))
                return
            if node.left:
                dfs(node.left, path+str(node.val)+'->')
            if node.right:
                dfs(node.right, path+str(node.val)+'->')
        if not root:
            return ""
        dfs(root, "")
        return paths