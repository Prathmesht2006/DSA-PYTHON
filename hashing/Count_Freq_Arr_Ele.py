class Solution:
    def countFrequencies(self, nums):
        freq={}
        for i in nums:
                freq[i]=freq.get(i,0)+1
        
        return [[num,count] for num,count in freq.items()]
