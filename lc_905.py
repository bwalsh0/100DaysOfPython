class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        sorted = []
        odd = []
        for i in A:
            if i % 2 is 0:
                sorted.append(i)
            else:
                odd.append(i)
        return sorted + odd
