from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter = {}
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sr, sc = i, j
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        k = len(litter)
        if k == 0:
            return 0
        full = (1 << k) - 1

        
        best = [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]
        best[sr][sc][0] = energy

        q = deque([(sr, sc, 0, energy)])
        steps = 0
        while q:
            for _ in range(len(q)):
                r, c, mask, e = q.popleft()
                if mask == full:
                    return steps
                if e == 0:
                    continue
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    ch = classroom[nr][nc]
                    if ch == 'X':
                        continue
                    ne, nm = e - 1, mask
                    if ch == 'L':
                        nm |= 1 << litter[(nr, nc)]
                    elif ch == 'R':
                        ne = energy
                    if ne > best[nr][nc][nm]:
                        best[nr][nc][nm] = ne
                        q.append((nr, nc, nm, ne))
            steps += 1
        return -1