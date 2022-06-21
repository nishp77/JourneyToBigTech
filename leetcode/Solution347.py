from typing import List


class Solution347:
    def topKFrequent(self, nums:List[int], k:int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq) - 1, 0,-1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result