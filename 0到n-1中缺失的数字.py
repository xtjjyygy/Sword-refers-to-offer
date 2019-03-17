'''
题目：一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0到n-1之内，在范围0到n-1内的n个数字中有且只有一个数字缺失，请找出这个数字
'''
#解法一：0到n-1之和减去数组之和
# -*- coding:utf-8 -*-
class Solution:
    def FindMissValue(self,data):
        return int((data[-1])*(data[-1]+1) / 2 - sum(data))

sol = Solution()
data = [0,1,2,3,4,5,6,7,8,9,10,11,12,14,15,16]
print(sol.FindMissValue(data))


#解法二：采用二分法
# -*- coding:utf-8 -*-
class Solution:
    def FindMissValue(self,data):
        if not data:
            return None
        first = 0
        end = len(data)-1
        while first <= end:
            mid = (end + first) // 2
            if data[mid] != mid:
                if mid == 0 or data[mid-1] == mid -1:
                    return mid
                end = mid - 1
            else:
                first = mid + 1
        if first == len(data):
            return len(data)
        return -1

sol = Solution()
data = [0,1,2,3,5,6]
print(sol.FindMissValue(data))
