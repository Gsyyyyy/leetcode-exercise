#b = nums[-1::-1].index(sorted_nums[b])； b = len(nums)-1-b从后往前索引并输出指针
#list.sort()是对当前list排序不会输出，输出用sorted()
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = []
        b = len(nums)-1 
        sorted_nums = sorted(nums)
        c = 0
        for i in range(b):
            sum = sorted_nums[c]+sorted_nums[b]
            if sum ==  target:
                c = nums.index(sorted_nums[c])
                b = nums[-1::-1].index(sorted_nums[b])
                b = len(nums)-1-b
                a = [c,b]
                break
            if sum < target:
                c += 1
            else:
                b-=1

        return a
