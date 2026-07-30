# Given an array arr of n elements. The task is to reverse the given array. The reversal of array should be inplace.

#inplace means make changes in original arr not in copy
# Example 

# Input: n=5, arr = [1,2,3,4,5]

# Output: [5,4,3,2,1]

class Solution:
    def reverse(self, arr: list) -> None:
        left=0
        right=len(arr)-1
        while left<right:
            arr[left],arr[right]=arr[right],arr[left]
            left=left+1
            right=right-1
        print(arr)




