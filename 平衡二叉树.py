'''
题目：输入一颗二叉树的根节点，判断该树是不是平衡二叉树，如果某二叉树的任意节点左右子树的深度相差不超过1，那么他就是一棵平衡二叉树。
'''

class Solution:

    def IsBalanced_Solution(self, pRoot):
        self.flag = True
        self.tree_Iteration(pRoot)
        return self.flag

    def tree_Iteration(self, pRoot):
        if not pRoot or self.flag==False:
            return 0
        left = self.tree_Iteration(pRoot.left)
        right = self.tree_Iteration(pRoot.right)
        if abs(left-right)>1:
            self.flag = False
        return left+1 if left>right else right+1
