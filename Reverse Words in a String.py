class Solution:
    def reverseWords(self, s: str) -> str:
        op = s.split()[::-1]
        result = []
        for i in op:
            result.append(i)
        return " ".join(result)