#!/usr/bin/env python3
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        if len(jewels)==0 or len(stones)==0:
            return 0
        jewels = set(jewels)
        j_count = 0
        for s in stones:
            if s in jewels:
                j_count+=1
        return j_count

## Approach:
# - Converting the string containing the jewels types into a set, since look up in a set takes O(1)
#
## Time Complexity:
# - O(j+s)
# - iterating through all j elements in the string jewels to form the corresponding set takes O(j)
# - Followed by iterating through all the elements of the stone string and check if it's in the jewel set takes O(s)
#
## Space Complexity:
# - O(1) in case you convert the jewel string into a set and store it in the same variable
# - O(n) in case you convert the jewel string into a set and store it in a different variable