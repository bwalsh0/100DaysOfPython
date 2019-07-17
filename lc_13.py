class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        
        roman = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i, char in enumerate(s):
            if len(s) == i + 1:
                total += roman.get(char)
                return total
            if char == "I" and (s[i+1]) == "X" or (s[i+1]) == "V" or\
            char == "X" and (s[i+1]) == "C" or (s[i+1]) == "D" or\
            char == "C" and (s[i+1]) == "L" or (s[i+1]) == "M":
                temp = char
                temp = str(char + s[i+1]) # jank 
                total += roman.get(temp)
            else:
                total += roman.get(char)
                  
        return total
