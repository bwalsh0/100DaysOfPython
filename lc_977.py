class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = []
        for i in A:
            result.append(i*i)
        result.sort()
        return result
