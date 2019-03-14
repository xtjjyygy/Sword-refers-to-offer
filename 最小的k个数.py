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
'''
另一种O(nlogk)的算法是基于堆排序的，特别适合处理海量数据。

我们可以先创建一个大小为k的数据容器来存储最小的k个数字，接下来我们每次从输入的n个整数中的n个整数中读入一个数。如果容器中已有的数字少于k个，则直接把这次读入的整数放入容器之中；如果容器已经有k个数字了，也就是容器满了，此时我们不能再插入新的数字而只能替换已有的数字。找出这已有的k个数中的最大值，然后拿这次待插入的整数和最大值进行比较。如果待插入的值比当前已有的最大值小，则用这个数替换当前已有的最大值；如果待插入的值比当前已有的最大值还要大，那么这个数不可能是最小的k个整数之一，于是我们可以抛弃这个整数。

因此当容器满了之后，我们要做3件事情：一是在k个整数中找到最大数；二是有可能在这个容器中删除最大数；三是有可能要插入一个新的数字。如果用一个二叉树来实现这个数据容器，那么我们在O(logk)时间内实现这三步操作。因此对于n个输入数字而言，总的时间效率就是O(nlogk)。
'''
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        res = []
        length = len(tinput)
        change = True
        if length <= 0 or k <= 0 or k > length:
            return res
        res = tinput[:k]
        for i in range(k, length + 1):
            if change == True:
                for j in range(0, k // 2 + 1)[::-1]:
                    self.HeadAdjust(res, j, k)
                for j in range(1, k)[::-1]:
                    res[0], res[j] = res[j], res[0]
                    self.HeadAdjust(res, 0, j)
                change = False
            if i != length and res[k - 1] > tinput[i]:
                res[k - 1] = tinput[i]
                change = True
        return res

    def HeadAdjust(self, input_list, parent, length):
        temp = input_list[parent]
        child = 2 * parent + 1
        while child < length:
            if child + 1 < length and input_list[child] < input_list[child + 1]:
                child += 1
            if temp >= input_list[child]:
                break
            input_list[parent] = input_list[child]
            parent = child
            child = 2 * parent + 1
        input_list[parent] = temp
