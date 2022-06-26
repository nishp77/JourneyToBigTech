class Solution5:
    def longestPalindrome(self, s:str) -> str:
        l,r = len(s) // 2 - 1, 0
        result = ""
        if len(s) % 2 == 0:
            r = len(s) // 2 
        else:
            r = len(s) // 2 + 1
            result += s[len(s) // 2]
        
        # index out of bound
        while s[l] == s[r] and l > -1 and r < len(s):
            result = ''.join((s[l], result, s[r]))
            l -= 1
            r += 1
        
        return result

s = Solution5()
s.longestPalindrome("cbbd")