'''
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
'''
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        for i in range(len(array)):
            temp = tsum - array[i]
            if temp in array[i+1:]:
                return [array[i],temp]
        return []
