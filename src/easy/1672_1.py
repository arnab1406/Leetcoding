class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for c in accounts:
            c_wealth = sum(c)
            if c_wealth > max_wealth:
                max_wealth = c_wealth
        return max_wealth
        