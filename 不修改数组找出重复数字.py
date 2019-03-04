'''
题目描述： 
在一个长度为n+1的数组里的所有数字都在1~n的范围内，所以数组中至少有一个数字是重复的。请找出数组中任意一个重复的数字，但是不能修改输入的数组。
'''
class Solution:

    def duplicate(self, numbers):
        if numbers == []:
            return False
        length = len(numbers)
        start = 1
        end = length -1
        while end >= start :
            middle = int((end-start)/2) + start
            count = self.countNum(numbers,length,start,middle)
            if end == start:
                if count >1 :
                    print True
                    return True
                else:
                    break
            if count > (middle - start) +1:
                end = middle
            else:
                start = middle+1
        return  False

    def countNum(self,numbers,length,start,end):
        count = 0
        for i in range(length):
            if numbers[i] <1 or numbers[i] >length :
                return False
            if  start<= numbers[i] <=end :
                count+=1
        return count
