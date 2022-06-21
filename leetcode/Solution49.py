from collections import defaultdict
from typing import List

class Solution49:
    def groupAnagrams(self, strs:List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            #making list of alphabet           
            count = [0] * 26

            for ch in s:
                #using ascii to calculate the index 
                count[ord(ch) - ord('a')] += 1

            result[tuple(count)].append(s)

        return result.values()


s = Solution49()
s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
