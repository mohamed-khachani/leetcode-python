class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        data = [""] * numRows
        chunk = 2 * numRows - 2

        for c in range(0, len(s) // chunk + 1):
            su = s[c * chunk : min(c * chunk + chunk, len(s))]
            i = 0
            pastchunk = False
            while i < len(su):
                if pastchunk:
                    data[2 * numRows - i - 2] += su[i]
                    i += 1
                    continue

                data[i] += su[i]
                i += 1
                if i == numRows:
                    pastchunk = True
            

        return ''.join(data)

print(Solution().convert("ABCDE", 5)) #