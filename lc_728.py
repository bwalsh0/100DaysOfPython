class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        flag = False
        for i in range(left, right+1):
            flag = False
            for c in str(i):
                if int(c) != 0 and i % int(c) == 0:
                    pass
                else:
                    flag = True
                    break
            if not flag:
                result.append(i)
            
        return result
    
    # Probably my worst performing solution yet
    
