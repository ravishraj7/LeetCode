class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) == k:
                res.append(path[:])
                return

            need = k - len(path)
            for num in range(start, n - need + 2):
                path.append(num)
                backtrack(num + 1)
                path.pop()

        backtrack(1)
        return res