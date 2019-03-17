'''
题目：请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度，假设字符串中指包含‘a’-‘z’的字符，例如，在字符串‘arabcacfr’中，组成的不含重复字符串的子字符串是‘acfr’，长度为4
'''

def longstSubstringWithoutDuplication(str):
    curLenght = 0
    maxLength = 0
    position = [-1]*26
    for i in range(len(str)):
        prevIndex = position[ord(str[i])-ord('a')]
        if prevIndex < 0 or i - prevIndex > curLenght:
            curLenght+=1
        else:
            if curLenght > maxLength:
                maxLength = curLenght
            curLenght = i - prevIndex
        position[ord(str[i])-ord('a')] = i
    if curLenght > maxLength:
        maxLength = curLenght
    return maxLength
if __name__ == '__main__':
    str = 'arabcacfr'
    print(longstSubstringWithoutDuplication(str))
