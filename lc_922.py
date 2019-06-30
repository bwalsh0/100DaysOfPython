# Slow solution but relatively straightforward; to make use of filter()

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:   
        odds = evens = result = []
        eIndex = oIndex = 0
        
        odds = list(filter(Solution.filterOdd, A))      
        evens = list(filter(Solution.filterEven, A))
        
        for i in range(len(A)):
            if i % 2 == 0:
                result.append(evens[eIndex])
                eIndex += 1
            elif i % 2 != 0:
                result.append(odds[oIndex])
                oIndex += 1
                
        return result
    
    def filterEven(A) -> bool:
        return (A % 2 == 0)
            
    def filterOdd(A) -> bool:
        return (A % 2 != 0) 
    
# Newer concepts: filter() function and iterator nuances (++i vs. += 1), etc.
