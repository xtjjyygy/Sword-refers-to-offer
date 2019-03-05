'''
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
'''

#效率低下的解法
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            return self.Fibonacci(n-1) + self.Fibonacci(n-2)
 #将结果存储在数组中的解法
 # -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        result = [0,1]
        if n<2:
            return result[n]
        if n > 1:
            for i in range(2, n+1):
                result.append(result[i-1] + result[i-2])
        return result[n]
                
