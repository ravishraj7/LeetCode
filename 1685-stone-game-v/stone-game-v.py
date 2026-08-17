class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + stoneValue[i]

        def rs(i, j):
            return pre[j + 1] - pre[i]

        g = [[0] * n for _ in range(n)]              
        rowPref = [[0] * n for _ in range(n)]      
        colSuf = [[0] * (n + 1) for _ in range(n)]    

        NEG = float('-inf')
        for j in range(n):
            colSuf[j][j + 1] = NEG
        for i in range(n):
            g[i][i] = stoneValue[i]
            rowPref[i][i] = stoneValue[i]
        for j in range(n):
            colSuf[j][j] = g[j][j]

        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1
                lo, hi = i, j - 1
                m = i - 1
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if rs(i, mid) <= rs(mid + 1, j):
                        m = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1

                best = 0
                if m >= i:
                    best = max(best, rowPref[i][m])
                    if m + 1 <= j - 1:
                        best = max(best, colSuf[j][m + 2])
                    if rs(i, m) == rs(m + 1, j):
                        best = max(best, g[m + 1][j])
                else:
                    best = max(best, colSuf[j][i + 1])

                dp_ij = best
                g[i][j] = dp_ij + rs(i, j)
                rowPref[i][j] = max(rowPref[i][j - 1], g[i][j])
                colSuf[j][i] = max(colSuf[j][i + 1], g[i][j])

        return g[0][n - 1] - pre[n]