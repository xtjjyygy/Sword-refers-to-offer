'''
题目：给定一个数字，我们按照如下规则把他翻译成字符串：0翻译成‘a'，1翻译成‘b'，....11翻译成‘l‘...25翻译成’z‘,一个数有可能有很多个翻译，如，12258有5种不同的翻译，分别是’bccfi‘、’bwfi‘、’bczi‘、’mcfi‘、’mzi‘。请编程实现一个函数，用来计算一个数字有多少种不同的翻译
'''

def GetTranslationCount(number):
    if number < 0:
        return 0
    numberInString = str(number)
    return otherGetTranslationCount(numberInString)

def otherGetTranslationCount(str_number):
    length = len(str_number)
    counts = [0]*length
    count = 0
    for i in range(length-1,-1,-1):
        count = 0
        if i < length -1:
            count = counts[i+1]
        else:
            count = 1
        if i <length-1:
            digit1 = int(str_number[i])
            digit2 = int(str_number[i+1])
            converted = digit1*10 +digit2
            if converted >= 10 and converted <=25:
                if i<length-2:
                    count+=counts[i+2]
                else:
                    count+=1
        counts[i]=count
    count = counts[0]
    return count

print(GetTranslationCount(152))
