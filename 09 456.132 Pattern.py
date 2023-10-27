from typing import List


class Solution:
    def hello(self):
    def find132pattern(self, nums: List[int]) -> bool:
        myStack = []
        for i in nums:
            if len(myStack) == 0 or myStack[-1] <= i:
                myStack.append(i)
            else:
                while len(myStack) != 0:
                    if myStack.pop() < i:
                        return True
                myStack.append(i)
        return False


a = Solution()
asdfasdf
nums = [3, 5, 0, 3, 4]

print(a.find132pattern(nums))
