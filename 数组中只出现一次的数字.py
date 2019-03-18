'''
题目描述
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字
'''
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if array == None:
            return []
        xor = 0
        for i in array:
            xor ^= i

        idxOf1 = self.getFirstIdx(xor)
        num1 = num2 = 0
        for j in range(len(array)):
            if self.IsBit(array[j], idxOf1):
                num1 ^= array[j]
            else:
                num2 ^= array[j]
        return [num1, num2]

    def getFirstIdx(self, num):
        idx = 0
        while num & 1 == 0 and idx <= 32:
            idx += 1
            num = num >> 1
        return idx

    def IsBit(self, num, indexBit):
        num = num >> indexBit
        return num & 1
