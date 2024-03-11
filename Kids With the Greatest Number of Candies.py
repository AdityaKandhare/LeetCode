class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        max_value = max(candies)
        for i in range(len(candies)):
            if (candies[i] + extraCandies >= max_value):
                output.append(True)
            else:
                output.append(False)
        return output


        