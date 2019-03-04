'''
题目描述
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        return s.replace(' ','%20')
#附：教材方法
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        if not isinstance(s, str) or len(s) <= 0 or s == None:
            return ''
        spaceNum = 0
        for i in s:
            if i == " ":
                spaceNum += 1
        
        newStrLen = len(s) + spaceNum * 2
        newStr = newStrLen * [None]
        indexOfOriginal, indexOfNew = len(s) - 1, newStrLen - 1
        while indexOfNew >= 0 and indexOfOriginal <= indexOfNew:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew - 2: indexOfNew + 1] = ['%', '2', '0']
                indexOfNew -= 3
                indexOfOriginal -= 1
            else: 
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        return ''.join(newStr)
