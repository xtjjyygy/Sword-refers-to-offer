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

#用位运算来改进PowerWithUnsignedExponent函数
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
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        result = self.PowerWithUnsignedExponent(base,exponent>>1)
        result *= result
        if exponent & 1 == 1:
            result*=base
        return result
sol = Solution()
print(sol.Power(base=2.0,exponent=3))
