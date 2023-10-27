from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                myStack.append(i)
            else:
                if len(myStack) == 0:
                    return False
                j = myStack.pop()
                if i == ')':
                    if j != '(':
                        return False
                elif i == '}':
                    if j != '{':
                        return False
                elif i == ']':
                    if j != '[':
                        return False
        if len(myStack) != 0:
            return False
        else:
            return True


a = Solution()

s = "(]"

print(a.isValid(s))
