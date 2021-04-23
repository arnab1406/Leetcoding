#!/usr/bin/env python3
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        if len(jewels)==0 or len(stones)==0:
            return 0
        return sum([1 for s in stones if s in jewels])

## Approach:
# - For each of the jewel in the string jewels, count the number of occurances in the string stones
#
## Time Complexity:
# - O(s*j)
# - Iterating through s elements in the stones string takes O(s)
# - Further, through j elements in the jewels string takes O(j)
#
## Space Complexity:
# O(s)
# A list is formed whose largest possible size is equal to the number of elements s in strings stones