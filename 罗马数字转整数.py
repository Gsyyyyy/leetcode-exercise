'''
罗马数字转整数
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        if 'IV' in s:
            s=s.replace('IV','')
            result+=4
        if 'IX' in s:
            s=s.replace('IX','')
            result+=9
        if 'XL' in s:
            s=s.replace('XL','')
            result+=40
        if 'XC' in s:
            s=s.replace('XC','')
            result+=90
        if 'CD' in s:
            s=s.replace('CD','')
            result+=400
        if 'CM' in s:
            s=s.replace('CM','')
            result+=900
        for i in s:
            match i:
                case 'M':result+=1000
                case 'D':result+=500
                case 'C':result+=100
                case 'L':result+=50
                case 'X':result+=10
                case 'V':result+=5
                case 'I':result+=1
                case _:return False
        return result