class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        best = [INF] * n      
        ans = INF
        left = 0
        cur = 0
        best_so_far = INF

        for right in range(n):
            cur += arr[right]
            while cur > target:
                cur -= arr[left]
                left += 1

            if cur == target:
                length = right - left + 1
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])
                best_so_far = min(best_so_far, length)

            best[right] = best_so_far

        return -1 if ans == INF else ans