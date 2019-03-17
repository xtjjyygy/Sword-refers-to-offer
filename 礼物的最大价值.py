'''
题目：
在一个m*n的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（大于0），你可以从棋盘的左上角开始那格子里的礼物，并每次向左或则向下移动一格，知道到达棋盘的右下角，给定一格棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物。
'''

class Solution:
    def getmaxValue(self, values, rows, cols):
        if not values or rows<=0 or cols <=0:
            return 0
        # 用于存放中间数值的临时数组
        temp = [0] * cols

        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0

                if i > 0:
                    up = temp[j]
                if j > 0:
                    left = temp[j-1]
                temp[j] = max(up,left) + values[i*rows+j]
        return temp[-1]
s = Solution()
a = s.getmaxValue([1,10,3,8,12,2,9,6,5,7,4,11,3,7,16,5],4,4)
print(a)
