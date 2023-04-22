'''
开始将l设为1000，值不够大，所以报错，后面设为正无穷float('inf')成功运行

给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。

 

示例 1：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
示例 2：

输入：nums = [0,0,0], target = 1
输出：0
 
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        result = 0
        nums.sort()
        if nums[0]+nums[1]+nums[2]>=target:
            return nums[0]+nums[1]+nums[2]
        l = 100000000000
        
        for i in range(len(nums)-2):
            
            z = i+1
            j = len(nums)-1
            while z<j:
                r = (nums[i]+nums[z]+nums[j])-target
                if  r < 0:
                    if l>(-r):
                        l = (-r)
                        result = nums[i]+nums[z]+nums[j]
                    z+=1
                elif r == 0:
                    result = nums[i]+nums[z]+nums[j]
                    return result
                else:
                    if l>r:
                        l = r
                        result = nums[i]+nums[z]+nums[j]
                    j-=1
        return result