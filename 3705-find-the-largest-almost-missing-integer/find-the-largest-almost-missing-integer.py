from collections import Counter
from typing import List

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

       
        if k == n:
            return max(nums)

      
        if k == 1:
            cnt = Counter(nums)
            candidates = [x for x in nums if cnt[x] == 1]
            return max(candidates) if candidates else -1

        
        def window_count(x):
            count = 0
            for i in range(n - k + 1):
                if x in nums[i:i + k]:
                    count += 1
            return count

        best = -1
        for x in {nums[0], nums[-1]}:
            if window_count(x) == 1:
                best = max(best, x)
        return best