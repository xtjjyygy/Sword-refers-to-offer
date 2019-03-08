class Solution:
    # def intToBin32(i):
    #     return (bin(((1 << 32) - 1) & i)[2:]).zfill(32)
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff #对32个二进制数据取补码
        while n != 0:
            count += 1
            n = (n - 1) & n
        return count
