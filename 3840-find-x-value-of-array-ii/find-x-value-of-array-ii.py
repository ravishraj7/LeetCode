class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1

        prod = [1] * (2 * size)
        cnt = [[0] * k for _ in range(2 * size)]

        def set_leaf(pos, val):
            i = size + pos
            v = val % k
            prod[i] = v
            cnt[i] = [0] * k
            cnt[i][v] = 1

        def merge(pa, ca, pb, cb):
            p = pa * pb % k
            c = ca[:]
            for r in range(k):
                if cb[r]:
                    c[(pa * r) % k] += cb[r]
            return p, c

        def pull(i):
            l, r = 2 * i, 2 * i + 1
            prod[i], cnt[i] = merge(prod[l], cnt[l], prod[r], cnt[r])

        for i in range(n):
            set_leaf(i, nums[i])
        for i in range(n, size):
            set_leaf(i, 1)
        for i in range(size - 1, 0, -1):
            pull(i)

        def update(pos, val):
            set_leaf(pos, val)
            i = (size + pos) // 2
            while i >= 1:
                pull(i)
                i //= 2

        def query(l, r):
            l += size
            r += size + 1
            left_parts, right_parts = [], []
            while l < r:
                if l & 1:
                    left_parts.append((prod[l], cnt[l]))
                    l += 1
                if r & 1:
                    r -= 1
                    right_parts.append((prod[r], cnt[r]))
                l >>= 1
                r >>= 1
            parts = left_parts + right_parts[::-1]
            p, c, first = 1, [0] * k, True
            for pp, cc in parts:
                if first:
                    p, c, first = pp, cc[:], False
                else:
                    p, c = merge(p, c, pp, cc)
            return c if not first else [0] * k

        ans = []
        for idx, val, start, x in queries:
            update(idx, val)
            ans.append(query(start, n - 1)[x])
        return ans