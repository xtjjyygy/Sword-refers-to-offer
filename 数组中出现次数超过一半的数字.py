'''
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

#方法一：用字典的键值对实现
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 0:
            return 0
        dict = {}
        for num in numbers:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] +=1
            if dict[num] > len(numbers) // 2:
                return num
        return 0
#方法二：用collections中的Counter实现
import collections
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        tmp = collections.Counter(numbers)
        x = len(numbers)/2
        for k, v in tmp.items():
            if v > x:
                return k
        return 0
#方法三：
'''
 思路：在遍历数组时保存两个值：一是数组中一个数字，一是次数。遍历下一个数字时，若它与之前保存的数字相同，则次数加1，否则次数减1；若次数为0，则保存下一个数字，并将次数置为1。遍历结束后，所保存的数字即为所求。然后再判断它是否符合条件即可。
 '''
 def MoreThanHalfNum_Solution(numbers):
    len1 = len(numbers)
    if len1==0:
        return 0
    elif len1>=1:
        # 遍历每个元素，并记录次数；若与前一个元素相同，则次数加1，否则次数减1
        res = numbers[0] # 初始值
        count = 1 # 次数
        for i in range(1,len1):
            if count == 0:
                # 更新result的值为当前元素，并置次数为1
                res = numbers[i]
                count = 1
            elif numbers[i] == res:
                count += 1 # 相同则加1
            elif numbers[i] != res:
                count -= 1 # # 不同则加1
 
        # 判断res是否符合条件，即出现次数大于数组长度的一半
        counts = 0
        for j in range(len1):
            if numbers[j] == res:
                counts += 1
        if counts>len1//2: # python3整除为//，python2为/
            return res
        else:
            return 0
#方法四：数组排序后，如果符合条件的数存在，则一定是数组中间那个数
def MoreThanHalfNum_Solution(numbers):
    len1 = len(numbers)
    if len1==0:
        return 0
    numbers.sort() # 排序
    middle = numbers[len1 // 2] #取排序后的中位数
 
    # 判断res是否符合条件，即出现次数大于数组长度的一半
    counts = 0
    for j in range(len1):
        if numbers[j] == middle:
            counts += 1
    if counts>len1//2:
        return middle
    else:
        return 0
        
