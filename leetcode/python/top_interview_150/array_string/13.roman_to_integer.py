class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN_CHAR_MAP = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,  
            "D": 500,
            "M": 1000
        }
        result = 0
        for i in range(len(s) - 1):
            if ROMAN_CHAR_MAP[s[i]] < ROMAN_CHAR_MAP[s[i + 1]]:
                result -= ROMAN_CHAR_MAP[s[i]]
            else:
                result += ROMAN_CHAR_MAP[s[i]]
            
        return result
        
case1_input = "III"
print(Solution().romanToInt(case1_input)) # 3

case2_input = "LVIII"
print(Solution().romanToInt(case2_input)) # 58

case3_input = "MCMXCIV"
print(Solution().romanToInt(case3_input)) # 1994
