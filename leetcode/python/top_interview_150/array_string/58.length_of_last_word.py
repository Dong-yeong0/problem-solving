class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
    

case1_input = "Hello World"
print(Solution().lengthOfLastWord(case1_input))

case2_input = "   fly me   to   the moon  "
print(Solution().lengthOfLastWord(case2_input))

case3_input = "luffy is still joyboy"
print(Solution().lengthOfLastWord(case3_input))
