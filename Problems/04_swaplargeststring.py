'''Given a string s, return the lexicographically largest string that can be 
obtained by swapping at most one pair of characters in s.
Examples: Input: s = "768" 
Output: "867" 
Explanation: Swapping the 1st and 3rd characters(7 and 8 respectively), 
gives the lexicographically largest string.using class and def'''

class Solution:
    def largestString(self, s: str) -> str:
        s = list(s)
        n = len(s)

        # Step 1: find rightmost maximum for each position
        max = [n - 1] * n
        for i in range(n - 2, -1, -1):
            max[i] = i if s[i] > s[max[i + 1]] else max[i + 1]

        # Step 2: find first place to swap
        for i in range(n):
            if s[i] < s[max[i]]:
                s[i], s[max[i]] = s[max[i]], s[i]
                break
        return "".join(s)

print(Solution().largestString("768"))   
print(Solution().largestString("333")) 