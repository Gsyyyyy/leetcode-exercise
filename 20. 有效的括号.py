'''
将所有左括号放到栈里面，遍历到右括号就用栈里面最后一个元素与之匹配，最后用栈是否为空判断
正误

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

'''
class Solution:
    def isValid(self, s: str) -> bool:
        bool = True
        i = 0
        list = []
        for i in s:
            if i in '({[':
                list.append(i)
            else:
                if i == ')':
                    if list == []:
                        return False
                    if list[len(list)-1]!='(':
                        return False
                    else: list.pop()
                if i == '}':
                    if list == []:
                        return False
                    if list[len(list)-1]!='{':
                        return False
                    else: list.pop()
                if i == ']':
                    if list == []:
                        return False
                    if list[len(list)-1]!='[':
                        return False
                    else: list.pop()
        if list!=[]:
            bool = False
        return bool