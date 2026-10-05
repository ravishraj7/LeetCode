class Solution:
    def checkValidString(self, s: str) -> bool:
        left, star = [], []
        for i, ch in enumerate(s):
            if ch == '(':
                left.append(i)
            elif ch == '*':
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
       
        while left and star:
            if left.pop() > star.pop():
                return False
        return not left        