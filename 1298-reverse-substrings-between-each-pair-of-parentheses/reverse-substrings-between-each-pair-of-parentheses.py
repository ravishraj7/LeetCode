class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        for ch in s:
            if ch == "(":
                stack.append("")
            elif ch == ")":
                inner = stack.pop()
                stack[-1] += inner[::-1]
            else:
                stack[-1] += ch
        return stack[-1]