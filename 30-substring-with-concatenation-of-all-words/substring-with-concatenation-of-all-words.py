from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        wl = len(words[0])
        num = len(words)
        total_len = wl * num
        n = len(s)
        if n < total_len:
            return []

        word_count = Counter(words)
        result = []

        for offset in range(wl):
            left = offset
            count = 0
            window = Counter()

            for right in range(offset, n - wl + 1, wl):
                word = s[right:right + wl]

                if word in word_count:
                    window[word] += 1
                    count += 1

                    while window[word] > word_count[word]:
                        left_word = s[left:left + wl]
                        window[left_word] -= 1
                        count -= 1
                        left += wl

                    if count == num:
                        result.append(left)
                        left_word = s[left:left + wl]
                        window[left_word] -= 1
                        count -= 1
                        left += wl
                else:
                    window.clear()
                    count = 0
                    left = right + wl

        return result