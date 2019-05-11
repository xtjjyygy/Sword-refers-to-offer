#总代码如下：包括数组转成二叉树，打印二叉树的前序、后序，中序遍历结果，对于不同遍历结果只需要改变BinaryTreeTraversal函数即可；
#coding=utf-8
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.result = []
    def ArrayToTree(self,nums):
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.ArrayToTree(nums[:mid])
        root.right = self.ArrayToTree(nums[mid+1:])
        return root

    def BinaryTreeTraversal(self,root):

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]
    root = Solution().ArrayToTree(nums=nums)
    result = Solution().BinaryTreeTraversal(root=root)
    print(result)


#前序遍历（递归）
    def BinaryTreeTraversal(self,root):
        if not root:
            return None
        self.result.append(root.val)
        self.BinaryTreeTraversal(root.left)
        self.BinaryTreeTraversal(root.right)
        return self.result
#前序遍历（非递归）
    def BinaryTreeTraversal(self,root):
        if not root:
            return None
        stack = [root]
        result = []

        while stack:
            result.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            root = stack.pop()
        return result

#在序遍历（递归）
    def BinaryTreeTraversal(self,root):
        if not root:
            return None
        self.BinaryTreeTraversal(root.left)
        self.result.append(root.val)
        self.BinaryTreeTraversal(root.right)
        return self.result

#在序遍历（非递归）   
    def BinaryTreeTraversal(self,root):
        if not root:
            return None
        stack = []
        sol = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                sol.append(curr.val)
                curr = curr.right
        return sol
