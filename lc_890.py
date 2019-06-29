class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ptFormat = []
        
        if len(pattern) == 1:
            return words
        for i in range(len(pattern) - 1):
            if (pattern[i] == pattern[i+1]):
                ptFormat.append(1)
            else:
                ptFormat.append(0)
                
        qualify = []
                
        for i in words:
            for j in range(len(pattern) - 1):
                if (i[j] == i[j+1]) and (ptFormat[j] == 0):
                    break
                elif (i[j] != i[j+1]) and (ptFormat[j] == 1):        
                    break
                elif (j == (len(pattern) - 2)):
                    qualify.append(i)
                    break
                    
                        
        return qualify
