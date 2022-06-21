# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
# 


class Solution191:
    def hammingWeight(self, n:int) -> int:
        result = 0
        while n:
            result += n & 1
            n >>= 1
        
        return result