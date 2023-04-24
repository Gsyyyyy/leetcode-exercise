'''
减少时间复杂度的方法是当abc遍历到的值与上一个相同时，continue循环

给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

 

示例 1：

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：

输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]

'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        result = []
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for l in range(i+1,len(nums)-2):
                if l>i+1 and nums[l]==nums[l-1]:
                    continue
                j = len(nums)-1

                for r in range(l+1,len(nums)-1):
                    if r>l+1 and nums[r]==nums[r-1]:
                        continue
                    while j>r and nums[i]+nums[l]+nums[r]+nums[j]>target:
                        j-=1
                    if r==j:
                        break
                    if nums[i]+nums[l]+nums[r]+nums[j]==target:
                        result.append([nums[i],nums[l],nums[r],nums[j]])



        return result        