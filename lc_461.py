class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        XOR = x ^ y
        counter = 0
        if x > y:
            n = x
        else:
            n = y
        
        for i in range(n.bit_length()):
            if ((XOR >> i) % 2) == 1:
                counter += 1
        return counter
    
# EXPLANATION:
#
# calculate bits of int for n
# 1 XOR 4 == 5
# count 1's by RHS 1 in a loop and modulo 2 and incr. counter
# 1001 >> 0  == 1001 % 2 == 1
# 1001 >> 1  == 0100 % 2 == 0
# 1001 >> 2  == 0010 % 2 == 0
# 1001 >> 3  == 0001 % 2 == 1
# total         counter  =  2
        
