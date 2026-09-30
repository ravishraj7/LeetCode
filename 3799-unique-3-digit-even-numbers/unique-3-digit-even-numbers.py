from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = Counter(digits)
        ans = 0
        for n in range(100, 1000, 2):
            need = Counter((n // 100, n // 10 % 10, n % 10))
            if all(cnt[d] >= c for d, c in need.items()):
                ans += 1
        return ans