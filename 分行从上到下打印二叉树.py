# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        queue = [root]
        result = []
        while queue:
            size = len(queue)
            currentLine = []
            for i in range(size):
                top = queue.pop(0)
                currentLine.append(top.val)
                if top.left:
                    queue.append(top.left)
                if top.right:
                    queue.append(top.right)
            result.append(currentLine)
        return result
                
