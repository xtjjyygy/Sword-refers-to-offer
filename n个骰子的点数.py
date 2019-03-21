'''
题目：把n个骰子扔在地上，所有骰子朝上一面的点数之和位s，输入n，打印出s的所有可能出现的值的概率
'''
#解法一：
g_maxValue = 6
def PrintProbability(number):
    if number < 1:
        return
    maxSum = number * g_maxValue
    pProbabilities = [0]*(maxSum-number+1)
    Probability(number,pProbabilities)
    total = g_maxValue** number
    for i in range(number,maxSum+1):
        ratio = float(pProbabilities[i-number]/total)
        print(i,ratio)
def Probability(number,pProbabilities):
    for i in range(1,g_maxValue+1):
        Probabilitytwo(number,number,i,pProbabilities)
def Probabilitytwo(original,current,sum,pProbabilities):
    if current == 1:
        pProbabilities[sum-original]+=1
    else:
        for i in range(1,g_maxValue+1):
            Probabilitytwo(original,current-1,i+sum,pProbabilities)
print(PrintProbability(1))

#解法二
g_maxValue = 6
def PrintProbability(number):
    if number< 1:
        return
    pProbabilities = [[0]*(g_maxValue*number+1) for i in range(2)]#定义二维数组
    flag = 0
    for i in range(1,g_maxValue+1):
        pProbabilities[flag][i] = 1
    for k in range(2,number+1):
        for i in range(k):
            pProbabilities[1-flag][i] = 0
        for i in range(k,g_maxValue*k+1):
            pProbabilities[1-flag][i]=0
            for j in range(1,min(i,g_maxValue)+1):
                pProbabilities[1-flag][i] += pProbabilities[flag][i-j]
        flag = 1-flag
    total = g_maxValue**number
    for i in range(number,g_maxValue*number+1):
        ratio = float(pProbabilities[flag][i]/total)
        print(i,ratio)
print(PrintProbability(1))
