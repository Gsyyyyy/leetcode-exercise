'''N 字形变换将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
 

示例 1：

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        list = ['' for _ in range(numRows)]
        count = 0
        for i in s:
            if numRows == 1:
                return s
            if count == numRows:
                count = -2
            if count == -numRows:
                count = 0
            if count >= 0:
                list[count]+=i
                count+=1
            else:
                list[count]+=i
                count-=1
        return ''.join(list)