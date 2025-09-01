class Solution:
    def topKFrequent(self, nums, k):
        count={}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num]=1
        sorted_nums=sorted(count.items(),key=lambda x:x[1],reverse=True)
        result=[]
        for i in range(k):
            result.append(sorted_nums[i][0])
        return result
    
#possible followup to do better than nlogn time
class Solution:
    def topKFrequent(self, nums, k):
        # Count frequencies
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Create buckets: index = frequency
        buckets = [[] for _ in range(len(nums)+1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        # Gather top k from buckets (from high freq to low)
        result = []
        for freq in range(len(buckets)-1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result


#learn later