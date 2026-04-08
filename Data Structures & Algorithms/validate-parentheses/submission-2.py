class Solution:
    def isValid(self, s: str) -> bool:
        map_ ={
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for c in s:
            if c in map_:
                if stack and stack[-1] == map_[c]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(c)

        return True if not stack else False

        