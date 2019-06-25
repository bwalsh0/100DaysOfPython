class Solution:  
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if not A:
            return A
        X = []
        result = []
        i = 0
        
        for y in A:
            X = []
            for x in reversed(y):
                if x is 0:
                    X.append(1)
                else:
                    X.append(0)
            result.append(X)
        
        return result
