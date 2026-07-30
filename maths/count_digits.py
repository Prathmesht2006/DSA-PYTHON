# You are given an integer n. You need to return the number of digits in the number.

class Solution:
    def countDigit(self, n):
        count=0
        while n>0:
            n=n//10
            count+=1
        return count
