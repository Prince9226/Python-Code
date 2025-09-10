''' Given a string n representing a Binary Number, The problem is to find its
decimal equivalent.
eg:- inpot: b=111
output: 7
expalin: 111 is 2**2+2**1+2**0=7.'''

class Solution:
    def binarytodecimal(self, b: str) -> int:
        decimal = 0
        pow = 0
        # process from right to left
        for digit in b[::-1]:
            if digit == '1':
                decimal += 2 ** pow
            pow += 1
        return decimal


# Example usage
s = Solution()
print(s.binarytodecimal("1010"))  # Output: 10
print(s.binarytodecimal("1111"))  # Output: 15
