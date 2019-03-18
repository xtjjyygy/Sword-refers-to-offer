'''
题目：在一个数组中除一个数字只出现一次之外，其他数字都出现了三次，请找出那个只出现一次的数字
'''
def FindNumAppearingOnece(numbers):
    if numbers == None or len(numbers)==0:
        return
    bitSum = [0]*32#int最多32位
    for i in range(len(numbers)):
        bitMask = 1
        for j in range(31,-1,-1):
            bit = numbers[i] & bitMask
            if bit !=0:
                bitSum[j]+=1
            bitMask = bitMask << 1
    result = 0
    for i in range(32):#用位运算求出只出现一次的那个数字
        result = result << 1
        result+=bitSum[i]%3
    return result

print(FindNumAppearingOnece([10,2,2,2]))
