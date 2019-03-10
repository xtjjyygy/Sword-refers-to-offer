# -*- coding:utf-8 -*-
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        ret = []
        path = []
        self.Find(root, expectNumber, ret, path)
        return ret
     
    def Find(self, root, target, ret, path):
        if not root:
            return
        path.append(root.val)
        isLeaf = (root.left is None and root.right is None)
        if isLeaf and target == root.val:
            ret.append(path[:])  # 这里这一步要千万注意啊， 
        if root.left:
            self.Find(root.left, target - root.val, ret, path)
        if root.right:
            self.Find(root.right, target - root.val, ret, path)
        path.pop()
