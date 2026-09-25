class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(expr, i):
            groups = [[]]  
            while expr[i] != '}':
                if expr[i] == '{':
                    s, i = parse(expr, i + 1)
                    groups[-1].append(s)
                elif expr[i] == ',':
                    groups.append([])
                    i += 1
                else:
                    j = i
                    while expr[j].isalpha():
                        j += 1
                    groups[-1].append({expr[i:j]})
                    i = j
            i += 1  

            result = set()
            for chain in groups:
                product = {''}
                for word_set in chain:
                    product = {a + b for a in product for b in word_set}
                result |= product
            return result, i

        words, _ = parse(expression + '}', 0)
        return sorted(words)