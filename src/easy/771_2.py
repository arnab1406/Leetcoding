#!/usr/bin/env python3
from collections import Counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        if len(jewels)==0 or len(stones)==0:
            return 0
        stones_c = Counter(stones)
        j_count = 0
        for j in jewels:
            j_count+=stones_c[j]
        return j_count

## Approach:
# - Convert the string containing stones into a Counter object
# - For each element of string jewels, the corresponding lookup of the count in stones_counter would be O(n)
#
## Time Complexity:
# - O(s+j)
# - Iterating through all s elements in the string stones to form the corresponding Counter object takes O(s)
# - Followed by iterating through all j the elements of the jewel string and check if it's count is present in the stones_counter object takes (j)
#
## Space Complexity:
# - O(1) in case you convert the stones string into a set and store it in the same variable
# - O(n) in case you convert the stones string into a set and store it in a different variable