# check whether the number is a palindrome number or not. Return true if it's a palindrome number, otherwise return false.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        left=0
        right=len(s)-1
    
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
            
        