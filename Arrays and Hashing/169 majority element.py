class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        max_key=max(count,key=count.get)
        return max_key
    

#possible follow up to do in o(1) space and o(n) time
#Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        candidate=None
        for num in nums:
            if count==0:
                candidate=num
            if candidate==num:
                count+=1
            else:
                count-=1
        return candidate