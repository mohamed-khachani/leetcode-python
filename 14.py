def commonPrefix(s1: str, s2: str) -> str:
        res = ""

        for a, b in zip(s1, s2):
            if a != b:
                break
            res += a

        return res


class Solution:    
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        c = commonPrefix(strs[0], strs[1])

        for i in range(2, len(strs)):
            if not strs[i].startswith(c):
                c = commonPrefix(c, strs[i])
                if len(c) == 0:
                    break

        return c

print(Solution().longestCommonPrefix(["dog","racecar","car"])) #