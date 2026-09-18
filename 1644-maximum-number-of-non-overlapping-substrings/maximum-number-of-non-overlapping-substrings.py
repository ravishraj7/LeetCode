class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first, last = {}, {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        def extend(c):
            start, end = first[c], last[c]
            i = start
            while i <= end:
                if first[s[i]] < start:
                    return None
                end = max(end, last[s[i]])
                i += 1
            return (start, end)

        intervals = []
        for c in first:
            iv = extend(c)
            if iv:
                intervals.append(iv)

        intervals.sort(key=lambda x: x[1])
        res, prev_end = [], -1
        for st, en in intervals:
            if st > prev_end:
                res.append(s[st:en + 1])
                prev_end = en
        return res