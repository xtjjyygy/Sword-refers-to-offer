'''
题目：给你一根长度位n的绳子，请把绳子剪成m段（m,n都是整数,n>1,m>1)，每根绳子的长度为，k[0],k[1],k[2]...k[m].请问k[0]×k[1]×k[2]...×k[m]的最大值为多少，例如：当n=8时，我们把它剪成2，3，3的三段，此时最大乘积为18
'''
class Solution:
    def maxProductAfterCutting(self,length):
        li = [0, 1, 2, 3]
        if length == 0:
            return 0
        if length == 1: 
            return 1
        if length == 2: 
            return 2
        if length == 3: 
            return 2
        for j in range(4, length + 1):
            max = 0
            for i in range(1, j):
                temp = li[i] * li[j - i]
                if temp > max:
                    max = temp
            li.append(max) 
        return li[-1]


sol = Solution()
print(sol.maxProductAfterCutting(8))
