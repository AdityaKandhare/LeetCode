class Solution:
    def reverseVowels(self, s: str) -> str:
        sample = "aeiouAEIOU"
        output = list(s)
        i = 0
        j = len(output) - 1 
        while i<j:
            if output[i] not in sample:
                i+=1
                continue
            if output[j] not in sample:
                j-=1
                continue
            output[i],output[j] = output[j], output[i]
            i+=1
            j-=1
        return "".join(output)