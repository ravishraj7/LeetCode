class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        n = len(s)
        result = []

        def is_valid(segment: str) -> bool:
            if len(segment) == 0 or len(segment) > 3:
                return False
            if segment[0] == '0' and len(segment) > 1:
                return False
            return int(segment) <= 255

        def backtrack(start: int, parts: list[str]):
            
            if len(parts) == 4:
                if start == n:
                    result.append('.'.join(parts))
                return

            
            remaining_parts = 4 - len(parts)
            remaining_chars = n - start
            if remaining_chars < remaining_parts or remaining_chars > remaining_parts * 3:
                return

            for length in range(1, 4):
                if start + length > n:
                    break
                segment = s[start:start + length]
                if is_valid(segment):
                    backtrack(start + length, parts + [segment])

        backtrack(0, [])
        return result