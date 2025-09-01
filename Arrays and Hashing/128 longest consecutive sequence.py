#one solution using nlogn time complexity
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums=sorted(set(nums))
        longest=1
        streak=1
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]==1:
                streak+=1
                longest=max(longest,streak)
            else:
                streak=1
        return longest
    
#followup question: can you do it in o(n) time complexity?
#using hashing
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        longest=0
        for num in numset:
            if num-1 not in numset:
                length=1
                while num+length in numset:
                    length+=1
                longest=max(longest,length)
        return longest