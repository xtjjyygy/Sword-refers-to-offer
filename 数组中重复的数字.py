# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        from collections import Counter
        a = Counter(numbers)
        for i in set(numbers):
            if a[i] > 1:
                duplication[0] = i
                return True
                break
        return False
