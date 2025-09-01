class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count={}
        for char in nums:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        for char in count:
            if count[char]>1:
                return True
        return False