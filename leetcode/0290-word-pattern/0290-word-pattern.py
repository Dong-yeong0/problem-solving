class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = list(s.split(" "))
        if len(pattern) != len(s):
            return False
        
        s2t, t2s = {}, {}
        for p, w in zip(pattern, s):
            if w not in s2t and p not in t2s:
                s2t[w] = p
                t2s[p] = w
            elif w not in s2t or s2t[w] != p:
                return False
        return True 