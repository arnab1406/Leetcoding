class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum,accounts))


## Time Complexity:
#
# O(n*m)
#
# Space Complexity:
#
# O(1)
#
# - Ideally, the time and space complexities should be similar to Approach 1
# - since the number of computations are the same and 
# - as we are not going for a list comprehension 
# - which would otherwise make our space complexity dependent on the size of the input