'''
TC: O(s*p)
SC: O(s*p)
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        plen = len(p)
        slen = len(s)
        
        if not plen and slen:
            return False
        
        dp = [[False for i in range(slen + 1)] for j in range(plen + 1)]
        dp[0][0] = True
        
        for i in range(1, plen + 1):
            if p[i - 1] == "*":
                dp[i][0] = dp[i - 1][0]
        
        for i in range(1, plen+1):
            for j in range(1, slen + 1):
                if p[i - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1] 
                elif p[i - 1] == "?" or p[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
        
        # print(dp)
        
        return dp[-1][-1]
        
        
        
        