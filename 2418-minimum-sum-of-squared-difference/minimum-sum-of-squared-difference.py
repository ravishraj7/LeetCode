class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        if sum(diffs) <= k:
            return 0

        max_d = max(diffs)
        cnt = [0] * (max_d + 1)
        for d in diffs:
            cnt[d] += 1
        for d in range(max_d, 0, -1):
            if cnt[d] == 0:
                continue
            if cnt[d] <= k:
                cnt[d - 1] += cnt[d]
                k -= cnt[d]
                cnt[d] = 0
            else:
                cnt[d - 1] += k
                cnt[d] -= k
                k = 0
                break

        return sum(d * d * c for d, c in enumerate(cnt))