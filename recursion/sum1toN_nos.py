class Solution:
    def NnumbersSum(self, N):
        if N==1:
            return 1
        return N+self.NnumbersSum(N-1)