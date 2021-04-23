# Credits: https://github.com/sriinampudi

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = 0
        for i in stones:
            if jewels.count(i) != 0:
                c = c+jewels.count(i)
                
        return(c)
        


            
            
            