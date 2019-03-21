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
    for i in range(number,maxSum+1):
        pProbabilities[i-number] = 0
    Probability(number,pProbabilities)
    total = g_maxValue** number
    for i in range(number,maxSum+1):
        ratio = float(pProbabilities[i-number]/total)
        print(i,ratio)
def Probability(number,pProbabilities):
    for i in range(g_maxValue+1):
        Probabilitytwo(number,number,i,pProbabilities)
def Probabilitytwo(original,current,sum,pProbabilities):
    if current == 1:
        pProbabilities[sum-original]+=1
    else:
        for i in range(g_maxValue+1):
            Probability(original,current-1,i+sum,pProbabilities)
print(PrintProbability(1))
