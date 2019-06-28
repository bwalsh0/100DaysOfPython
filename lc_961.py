class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        A.sort()
        j = 1
        for x in range(len(A)):
            if A[x] == A[j]:
                return A[x]  
            if (j < len(A) - 1 and x < len(A) - 1):
                x += 2
                j = x+1
            else:
                return A[x+1]
            
# There is a more efficient solution using Python's built-in collection library
