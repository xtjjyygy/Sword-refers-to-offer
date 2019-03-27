'''
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''

# -*- coding:utf-8 -*-
class Solution:
    def Power(self,base,exponent):
        g_invalidinput = False
        if base == 0.0 and exponent < 0:
            g_invalidinput = True
            return 0.0
        absExponent = abs(exponent)
        result = self.PowerWithUnsignedExponent(base,absExponent)
        if exponent < 0:
            result = 1.0/result
        return result
    def PowerWithUnsignedExponent(self,base,exponent):
        result = 1.0
        for i in range(1,exponent+1):
            result*=base
        return result
