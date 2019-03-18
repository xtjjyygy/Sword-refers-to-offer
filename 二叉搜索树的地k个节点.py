'''
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
'''

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        global res
        if not pRoot or not k:
            return 
        res = []
        self.traverse(pRoot,k)
        if len(res) < k:
            return
        return res[k-1]
    def traverse(self,node,k):
        if not node:
            return
        self.traverse(node.left,k)
        res.append(node)
        self.traverse(node.right,k)
