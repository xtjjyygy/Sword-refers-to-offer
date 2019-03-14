'''
题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
'''
#方法一：取任意一个数，用递归的方法将小于此数的所有数放在左边，大于次数的数放在右边
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k > len(tinput):
            return []
        tinput = self.TreeSort(tinput)
        return tinput[:k]
    def TreeSort(self,l):
        if not l:
            return []
        LNode = l[0]
        left = self.TreeSort([x for x in l[1:] if x < LNode])
        right = self.TreeSort([x for x in l[1:] if x >= LNode])
        return left + [LNode] + right
