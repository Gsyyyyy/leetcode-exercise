'''
第二个不对，超出了时间界限

当前左右括号都有大于 00 个可以使用的时候，才产生分支；
产生左分支的时候，只看当前是否还有左括号可以使用；
产生右分支的时候，还受到左分支的限制，右边剩余可以使用的括号数量一定得在严格大于左边剩余的数量的时候，才可以产生分支；
在左边和右边剩余的括号数都等于 00 的时候结算。

'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        signpost = ''
        l = r = n
        def travel(signpost, l, r):
            if l == 0 and r == 0:
                result.append(signpost)
                return 
            if r<l:
                return
            if l>0 :
                travel(signpost+'(',l-1,r)
                
            if r>0:
                travel(signpost+')',l,r-1)

        travel(signpost,l,r)
        return result
    


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        signpost = ''
        l = r = n
        def travel(signpost, l, r):
            if l == 0 and r == 0:
                result.append(signpost)
                return 
            
            if l>0 :
                travel(signpost+'(',l-1,r)
                travel(signpost+')',l,r-1)
            else:
                travel(signpost+'(',l-1,r)

        travel(signpost,l,r)
        return result