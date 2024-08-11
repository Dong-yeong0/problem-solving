class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map_s_to_t = {}
        map_t_to_s = {}
                
        for i in range(len(s)):
            original = s[i]
            replacement = t[i]
            
            if original in map_s_to_t:
                if map_s_to_t[original] != replacement:
                    return False
            else:
                map_s_to_t[original] = replacement
            
            if replacement in map_t_to_s:
                if map_t_to_s[replacement] != original:
                    return False
            else:
                map_t_to_s[replacement] = original
                
        return True