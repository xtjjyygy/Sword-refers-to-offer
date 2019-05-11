'''
题目：将list转换成二叉树，并按层遍历输出对应值
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        stack = []
        result = []
        stack.append(root)
        while len(stack)>0:
            currentRoot = stack.pop(0)
            result.append(currentRoot.val)
            if currentRoot.left:
                stack.append(currentRoot.left)
            if currentRoot.right:
                stack.append(currentRoot.right)
        return result

if __name__ == '__main__':
    root = Solution().sortedArrayToBST(nums=[1,2,3,4,5,6,7])
    result = Solution().PrintFromTopToBottom(root=root)
    print(result)
