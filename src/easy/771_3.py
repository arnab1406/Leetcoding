#!/usr/bin/env python3
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        if len(jewels)==0 or len(stones)==0:
            return 0        
        j_count = 0
        for j in jewels:
            j_count+=stones.count(j)
        return j_count


## Approach:
# - For each of the jewel in the string jewels, count the number of occurances in the string stones
#
## Time Complexity:
# - O(j+s)
# - Iterating through j elements in the jewels string takes O(j)
# - Further, count operation takes place in 0(s) for s elements in the stones string. Reference: https://stackoverflow.com/questions/35855748/whats-the-computational-cost-of-count-operation-on-strings-python
#
## Space Complexity:
# O(1)
# Neither dependent on length of jewels string nor on length of stones string