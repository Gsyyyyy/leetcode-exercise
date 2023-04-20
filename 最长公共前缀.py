'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

 

示例 1：

输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        d = ''
        bool = True
        a = 0
        while 1:
            if a == len(strs[0]):
                break
            d = strs[0][a]
            for i in range(len(strs)):
                if a >= len(strs[i]):
                    s = ''
                else:s = strs[i][a]
                if s != d:
                    bool = False
            if bool == True:
                result+=strs[0][a]
                a+=1
            else:break
        if len(result)==0:
            return ''
        else:
            return result
