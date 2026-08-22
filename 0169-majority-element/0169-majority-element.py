class Solution(object):
    def majorityElement(self, nums):
        count=0
        result=None
        for i in nums:
            if count==0: 
                result=i
            if result==i:
                count+=1
            else:
                count-=1
        return result
            

        