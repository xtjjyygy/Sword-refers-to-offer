'''
题目描述
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
'''
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1

        store = {}
        lis = list(s)

        for i in lis:
            if i not in store.keys():
                store[i] = 0
            store[i] += 1

        for i in lis:
            if store[i] == 1:
                return s.index(i)

        return -1
sol = Solution()
print(sol.FirstNotRepeatingChar(s='abaccdeff'))
