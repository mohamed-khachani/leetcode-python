
open_brackets = ['(', '[', '{']
closing_brackets = [')', ']', '}']

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in open_brackets:
                stack.append(char)

            else:
                if len(stack) == 0:
                    return False

                last = stack.pop()

                if open_brackets.index(last) != closing_brackets.index(char):
                    return False

        return len(stack) == 0


print(Solution().isValid("(){}}{"))