'''
题目：数组中数值和下标相等的元素
假设一个单调递增的数组里的每一个元素都是整数并且是唯一的。请编程实现一个函数，找出数组中任意一个数值等于其下标的元素，例如：在[-3,-1,1,3,5]中，返回3
'''
class Solution:
    def FindSubscriptEqual(self,data):
        if not data:
            return 0
        low = 0
        high = len(data)-1
        while low<=high:
            mid = (low+high)//2
            if mid < data[mid]:
                high = mid -1
            elif mid > data[mid]:
                low = mid+1
            else:
                return mid
        return -1
sol = Solution()
print(sol.FindSubscriptEqual(data=[-3,-1,0,1,4,5,7,8]))
