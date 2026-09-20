class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i, c in enumerate(s, start=1):
            total += (26 - (ord(c) - ord('a'))) * i
        return total