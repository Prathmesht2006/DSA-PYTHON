class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxCount=0
        current=0
        for i in nums:
            if i==1:
                current+=1
                maxCount=max(current,maxCount)
            else:
                current=0

        return maxCount