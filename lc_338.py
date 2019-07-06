class Solution:
    def countBits(self, num: int) -> List[int]:
        total = []
        for i in range(num + 1):
            counter = bin(i).count('1')
            # for j in bin(i):
            #     if j == '1':
            #         counter += 1
            total.append(counter)
            
        return total
        
        # bin(i).count('1') is the easy way to do it with built in functions
        # for loop to search each char in the returned string is slower
        
