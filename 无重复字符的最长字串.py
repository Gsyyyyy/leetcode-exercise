'''给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = ''
        count = 0
        fcount = 0
        list1 = []
        for i in range(len(s)):
            count+=1
            a+=s[i]
            if a.count(s[i],0,len(a)) == 2:
                fcount, count= count-1, len(a)-a.index(s[i])-1
                list1.append(fcount)
                a = a[a.index(s[i])+1:]
            else:
                fcount = count
        list1.append(fcount)
        if fcount == len(s):
            return len(s)
        fcount = max(list1)
        return fcount