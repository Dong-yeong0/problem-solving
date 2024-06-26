class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index, t_index = 0, 0
        s_len, t_len = len(s), len(t)
        
        while t_index < t_len:
            if s_index < s_len and s[s_index] == t[t_index]:
                s_index += 1

            t_index += 1

        return s_index == s_len