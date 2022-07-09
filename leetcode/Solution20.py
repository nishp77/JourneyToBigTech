class Solution20:
    def isValid(self, s:str) -> bool:
        stack  = []
        m = {")" : "(", "}" : "{", "]" : "["}


        for c in s:
            if c in m:
                if stack and stack[-1] == m[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False