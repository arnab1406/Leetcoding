#!/usr/bin/env python3
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for c in accounts:
            c_wealth = sum(c)
            if c_wealth > max_wealth:
                max_wealth = c_wealth
        return max_wealth

# # Approach:
#
# - Set a counter variable to keep track of the max wealth possessed by a customer
# - Iterate through each of the _list of customer account_ in our __list of list of customer accounts__
# - Compute the summation of all the amounts a customer has across their accounts
# - If this sum is greater than the value of our max wealth counter variable, update the max wealth counter variable with the value of this sum i.e. total wealth of a customer c
# - Return the last known value of max wealth counter variable
#
# Time Complexity:
#
#  - O(n * m)
# - Iterating through each element of the list of n customers takes O(n)
# - Further, for each customer c, iterating through all of their m bank accounts to compute their total wealth takes O(m)

# Space Complexity:
# 
# - O(1)
# - As it is not dependent on the size of the input list unless it is very large