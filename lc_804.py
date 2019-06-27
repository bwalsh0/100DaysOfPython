class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                 "....","..",".---","-.-",".-..","--","-.",
                 "---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."] 
        alpha = "abcdefghijklmnopqrstuvwxyz"
        toMorse = []
        
        dct = {i: j for i,j in zip(alpha, MORSE)}
        
        for word in words:
            toMorse.append(''.join(list(map(dct.get, list(word)))))
        
        return len(set(toMorse))
    
    # zip() -> pairs each MORSE[i] with alpha[i] to toMorse[(x, y), (x, y)...]
    # dct.get -> returns the value of each pair, where x maps to y in (x: y)
