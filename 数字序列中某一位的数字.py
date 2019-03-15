'''
数字以0123456789101112131415...的格式序列化到一个字符序列中。在这个序列中，第5位（从0开始计数）是5 ，第13位是1，第19位是4，等等。请写一个函数，求任意第n位的对应数字； 
'''
#方法一：

def aa(n,q):
    m=str(n)
    
    for k,s in enumerate(m):
        if k==q:
            return s
#方法二：剑指offer上面的方法
def digitAtIndex(index):
    if index<0:
        return -1
    digits = 1
    while True:
        numbers = countOfIntergers(digits)
        if index < numbers*digits:
            return otherdigitAtIndex(index,digits)
        index -=digits*numbers
        digits+=1
    return -1

def countOfIntergers(digits):
    if digits == 1:
        return 10
    count = int(10**(digits-1))
    return 9*count

def otherdigitAtIndex(index , digits):
    number = beginNumber(digits) + index//digits#取整
    indexFromRight = digits - index % digits
    for i in range(1,indexFromRight):
        number //=10#取整
    return number%10

def beginNumber(digits):
    if digits == 1:
        return 0
    return int(10**(digits-1))


print(digitAtIndex(5))
