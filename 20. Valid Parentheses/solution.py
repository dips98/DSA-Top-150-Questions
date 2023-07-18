class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openPars = ['[', '(', '{']
        closePars = [']', ')', '}']
        for i in s:
            if i in openPars:
                stack.append(i)
            elif i in closePars:
                if not stack:
                    return False
                if closePars.index(i) != openPars.index(stack.pop()):
                    return False
            else:
                return False
        return len(stack) == 0