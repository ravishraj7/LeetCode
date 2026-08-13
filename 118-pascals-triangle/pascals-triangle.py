class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        for row in range(numRows):
            current = [1] * (row + 1)

            for j in range(1, row):
                current[j] = triangle[row - 1][j - 1] + triangle[row - 1][j]

            triangle.append(current)
        return triangle
        