class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def check(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            match = False

            if i < len(s):
                if s[i] == p[j] or p[j] == '.':
                    match = True

            if j + 1 < len(p) and p[j + 1] == '*':

                skip = check(i, j + 2)

                repeat = False

                if match:
                    repeat = check(i + 1, j)

                result = skip or repeat

            else:
                if match:
                    result = check(i + 1, j + 1)
                else:
                    result = False

            memo[(i, j)] = result
            return result

        return check(0, 0)

print(Solution().isMatch('aa', 'a'))