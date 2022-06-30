class Solution424:
    def characterReplacement(self, s:str, k:int) -> int:
        occurence = {}
        result = 0
        l = 0
        for r in range(len(s)):
            occurence[s[r]] = 1 + occurence.get(s[r], 0)

            while (r-l+1) - max(occurence.values()) > k:
                occurence[s[l]] -= 1
                l += 1

            result = max(result, r-l+1)

        return result