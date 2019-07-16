class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = ""
        numOpen = 0
        
        for i in S:
            if i == '(' and numOpen > 0:
                result += i
            if i == ')' and numOpen > 1:
                result += i
            if i == '(':
                numOpen += 1
            else: 
                numOpen -= 1
                
        return result
