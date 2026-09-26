class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        line = []
        line_len = 0
        
        for word in words:
            # Check if adding this word (plus a space) exceeds maxWidth
            if line_len + len(line) + len(word) > maxWidth:
                # Justify current line
                result.append(self._justify(line, line_len, maxWidth))
                line = []
                line_len = 0
            line.append(word)
            line_len += len(word)
        
        # Last line: left-justified
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result
    
    def _justify(self, line: list[str], line_len: int, maxWidth: int) -> str:
        if len(line) == 1:
            return line[0] + ' ' * (maxWidth - line_len)
        
        total_spaces = maxWidth - line_len
        gaps = len(line) - 1
        space, extra = divmod(total_spaces, gaps)
        
        justified = ''
        for i, word in enumerate(line[:-1]):
            justified += word + ' ' * (space + (1 if i < extra else 0))
        justified += line[-1]
        
        return justified