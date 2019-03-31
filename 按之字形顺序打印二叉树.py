'''
题目描述
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot==None:
            return []
        odd=[]
        even=[]
        res=[]
        odd.append(pRoot)
        while odd or even:
            r=[]
            while odd:
                temp=odd.pop()
                r.append(temp.val)
                if temp.left:
                    even.append(temp.left)
                if temp.right:
                    even.append(temp.right)
            if r:
                res.append(r)
            r=[]
            while even:
                temp=even.pop()
                r.append(temp.val)
                if temp.right:
                    odd.append(temp.right)
                if temp.left:
                    odd.append(temp.left)
            if r:
                res.append(r)
        return res
