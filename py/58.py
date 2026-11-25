class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])

print(Solution().lengthOfLastWord("luffy is still joyboy")) # :) :)