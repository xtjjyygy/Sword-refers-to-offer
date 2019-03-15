'''
题目描述
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
'''
#方法：用最大堆和最小堆
import heapq
class Solution:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.flag = 1
    def Insert(self, num):
        # write code here
        if self.flag:
            if self.minHeap == [] or num <= self.minHeap[0]: #插入最大堆
                self.maxHeap.append(num) #插入
                heapq._heapify_max(self.maxHeap) #调整，必须使用_heapify_max，而不是heapify
            elif num > self.minHeap[0]:  #大于最小堆最小元素，需要插入到最小堆，并且替换
                self.maxHeap.append(heapq.heappop(self.minHeap))
                heapq._heapify_max(self.maxHeap)
                heapq.heappush(self.minHeap, num)
            self.flag = 0
        else:
            if self.maxHeap == [] or num >= self.maxHeap[0]:  #插入最小堆
                heapq.heappush(self.minHeap, num)
            elif num < self.maxHeap[0]: #插入最大堆，并把最大堆的根替换到右边的最小堆
                heapq.heappush(self.minHeap, heapq.heappop(self.maxHeap))  #最大堆的根
                self.maxHeap.append(num)
                heapq._heapify_max(self.maxHeap)
            self.flag = 1
    def GetMedian(self,demo):
        # write code here
        if self.flag:
            return float('{:.2f}'.format((self.maxHeap[0] + self.minHeap[0]) / 2.0))
        else:
            return float('{:.2f}'.format(self.maxHeap[0]))
sol = Solution()
sol.Insert(5)
print(sol.GetMedian())
sol.Insert(2)
print(sol.GetMedian())
sol.Insert(3)
print(sol.maxHeap)
print(sol.minHeap)
print(sol.GetMedian())
sol.Insert(4)
print(sol.GetMedian())
sol.Insert(1)
print(sol.GetMedian())
sol.Insert(6)
print(sol.GetMedian())
sol.Insert(7)
print(sol.GetMedian())
sol.Insert(0)
print(sol.GetMedian())
sol.Insert(8)
print(sol.maxHeap)
print(sol.minHeap)
print(sol.GetMedian())        
