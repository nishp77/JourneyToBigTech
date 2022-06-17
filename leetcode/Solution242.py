class Solution242:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        for o in countS:
            if countS[o] != countT.get(o, 0):
                return False
        
        return True

a = Solution242()
a.isAnagram("rat", "car")