class Solution:
    def defangIPaddr(self, address: str) -> str:
        nums = address.split('.')
        
        return "[.]".join(nums)
        
        # Another LC problem that can be solved with 1-2 lines in Python
        # .split() separates the address into array elements by the '.' character.
        # "[.]".join(arr) re-assembles the array into a string and inserts "[.]" between each element
        
