#Binary Tree Traversals




# ******* PREORDER ***********
#Preorder (Root, Left, Right)

#Recursive 

def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


#Iterative
def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return
    ans=[]
    q = [root]
    while q:
        node = q.pop()
        ans.append(node.val)
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)
    return ans



# ************** IN ORDER ******************
#Inorder (Left, Root, Right) 

#Recursive
def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
         


#Iterative


def inorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """ 
    stack = []
    ans = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            ans.append(node.val)
            node = node.right
    return ans



# *************** POSTORDER *****************


# Postorder (Left, Right, Root)


#Recursive

 def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root:
            return []
        
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]




# Iterative 

#root > right > left, reverse result, which is bottom of left up, bottom of right up, root
def postorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if not root:
        return 
    ans = []
    stack =[root]
    while stack:
        node = stack.pop()
        ans.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return ans[::-1]

































