# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        ret = []
        path = []
        self.Find(root,expectNumber,ret,path)
        return ret
    
    def Find(self,root,expectNumber,ret,path):
        if not root:
            return []
        path.append(root.val)
        isleaf = (root.right == None and root.left == None)
        if isleaf and expectNumber == root.val:
            ret.append(path[:])
        if root.left:
            self.Find(root.left,expectNumber-root.val,ret,path)
        if root.right:
            self.Find(root.right,expectNumber-root.val,ret,path)
        path.pop()
