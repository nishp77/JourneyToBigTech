from typing import List


class Solution739:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            
            stack.append([t,i])
        
        return res


s = Solution739()
s.dailyTemperatures([73,74,75,71,69,72,76,73])