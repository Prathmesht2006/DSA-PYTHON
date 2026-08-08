class Solution:
    def isPalindrome(self, s):
        s="".join(i.lower() for i in s if i.isalnum())
        def check(left,right):
            if left>=right:
                return True

            if s[left]!=s[right]:
                return False
            return check(left+1,right-1)
        
        return check(0,(len(s)-1))
