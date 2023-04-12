'''TypeError: list indices must be integers or slices, not float
    return float((nums1[len(nums1)/2]+nums1[len(nums1)/2-1])/2)
Line 7 in findMedianSortedArrays (Solution.py)
    ret = Solution().findMedianSortedArrays(param_1, param_2)
Line 35 in _driver (Solution.py)
    _driver()
Line 46 in <module> (Solution.py)
列表的声明[]内必须为整数不能是浮点数，哪怕用/计算结果为整数也得用//向下取整
'''
import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if (len(nums1) % 2) == 0:
            return float((nums1[len(nums1)//2]+nums1[len(nums1)//2-1])/2)
        else:
            return float(nums1[math.floor(len(nums1)/2)])