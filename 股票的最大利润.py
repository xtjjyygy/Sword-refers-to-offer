'''
题目：假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少，例如，一只股票在某些时间节点的价格为{9，11，8，5，7，12，16，14}。如果我们能在价格为5的时候买入并在价格为16的时候卖出，则能获得最大的利润11.
'''
# -*- coding:utf-8 -*-
class Solution:
    def MaxDiff(self, number):
        # write code here
        if not number or len(number) < 2:
            return 0
        min = number[0]
        maxDiff = number[1] - min
        for i in range(2,len(number)):
            if number[i-1] < min:
                min = number[i-1]
            currentDiff = number[i]-min
            if currentDiff > maxDiff:
                maxDiff = currentDiff
        return maxDiff
sol = Solution()
print(sol.MaxDiff(number=[2,3,1,10,4,11]))
