from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=[1]*len(nums)
        rp=1
        lp=1
        for i in range(len(nums)):
            a[i]*=lp
            lp*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            a[i]*=rp
            rp*=nums[i]
        return a
    
#super easy to understand algorithm using prefix product and suffix product