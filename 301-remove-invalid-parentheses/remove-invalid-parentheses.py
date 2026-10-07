from collections import deque
from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(t: str) -> bool:
            count = 0
            for ch in t:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        visited = {s}
        result = []
        found = False

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if is_valid(curr):
                    result.append(curr)
                    found = True
                if found:
                    continue  
                for i in range(len(curr)):
                    if curr[i] not in '()':
                        continue
                    nxt = curr[:i] + curr[i + 1:]
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
            if found:
                break

        return result