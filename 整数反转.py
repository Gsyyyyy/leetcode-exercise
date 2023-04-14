'''整数反转
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
 

示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0
'''
class Solution:
    def reverse(self, x: int) -> int:
        a = 1
        if x < 0:
            a = -1
            x = -x
        st = []
        for s in str(x):
            st.append(s)
        output = ''.join(reversed(st))
        output = int(output)*a
        return output if output >= (-1)*(2**31) and output <= (2**31)-1 else 0