class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(':')','{':'}','[':']'}
        stack = []
        for i in s:
            if i in mapping:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                if mapping[stack.pop()] != i:
                    return False

        return len(stack) == 0

                
        