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
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        n = len(tinput)
        if k <= 0 or k > n:
            return list()
        start = 0
        end = n - 1
        mid = self.partition(tinput, start, end)
        while k - 1 != mid:
            if k - 1 > mid:
                start = mid + 1
                mid = self.partition(tinput, start, end)
            elif k - 1 < mid:
                end = mid - 1
                mid = self.partition(tinput, start, end)
        res = tinput[:mid+1]
        # res.sort()
        return res
        
    def partition(self, numbers, low, high):
        key = numbers[low]
        while low < high:
            while low < high and numbers[high] >= key:
                high -= 1
            numbers[low] = numbers[high]
            while low < high and numbers[low] <= key:
                low += 1
            numbers[high] = numbers[low]
        numbers[low] = key
        return low
#方法二：建立二叉树，最大堆
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        n = len(tinput)
        if k <= 0 or k > n:
            return list()
        # 建立大顶堆
        for i in range(int(k / 2) - 1, -1, -1):
            self.heapAjust(tinput, i, k - 1)
        for i in range(k, n):
            if tinput[i] < tinput[0]:
                tinput[0], tinput[i] = tinput[i], tinput[0]
                # 调整前k个数
                self.heapAjust(tinput, 0, k - 1)
        print(tinput[:k])
 
    def heapAjust(self, nums, start, end):
        temp = nums[start]
        # 记录较大的那个孩子下标
        child = 2 * start + 1
        while child <= end:
            # 比较左右孩子，记录较大的那个
            if child + 1 <= end and nums[child] < nums[child + 1]:
                # 如果右孩子比较大，下标往右移
                child += 1
            # 如果根已经比左右孩子都大了，直接退出
            if temp >= nums[child]:
                break
            # 如果根小于某个孩子,将较大值提到根位置
            nums[start] = nums[child]
            # nums[start], nums[child] = nums[child], nums[start]
            # 接着比较被降下去是否符合要求，此时的根下标为原来被换上去的那个孩子下标
            start = child
            # 孩子下标也要下降一层
            child = child * 2 + 1
        # 最后将一开始的根值放入合适的位置(如果前面是交换，这句就不要)
        nums[start] = temp
