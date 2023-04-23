'''
函数遍历

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。



 

示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]
 
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        datalist={'2':'abc',
                  '3':'def',
                  '4':'ghi',
                  '5':'jkl',
                  '6':'mno',
                  '7':'pqrs',
                  '8':'tuv',
                  '9':'wxyz'}
        result = []
        def numTravel(combination,next_digits):
            if len(next_digits) == 0:
                result.append(combination)
            else:
                for i in  datalist[next_digits[0]]:
                    numTravel(combination+i,next_digits[1:])
        numTravel('',digits)
        if digits == '':
            result = []
        return result