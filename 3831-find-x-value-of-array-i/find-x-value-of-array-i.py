class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        res = [0] * k
        cnt = [0] * k 

        for a in nums:
            m = a % k
            new = [0] * k
            new[m] += 1                      
            for r in range(k):
                if cnt[r]:
                    new[(r * m) % k] += cnt[r] 
            cnt = new
            for r in range(k):
                res[r] += cnt[r]

        return res