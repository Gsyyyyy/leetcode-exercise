class Solution:
    def longestPalindrome(self, s: str) -> str:
        hash = {}
        s2 = []
        list3 = []
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                s2 = ''.join(reversed(s[i:j]))
                if s2 == s[i:j]:
                   hash[len(s[i:j])] = s[i:j]
                   list3.append(len(s[i:j]))
        return hash[max(list3)]
if __name__=='__main__':
    s= "babad"
    a = Solution()
    print(a.longestPalindrome(s))


class Solution:
    def longestPalindrome(self, s: str) -> str:
        hash = {}
        s2 = []
        list3 = []
        longest_palindrome = ''
        for i in range(len(s)-1,-1,-1):
            for j in range(i+1,len(s)):
                if j-i+1<len(longest_palindrome):
                    break
                s2 = ''.join(reversed(s[i:j]))
                if s2 == s[i:j]:
                   if j-i+1>len(longest_palindrome):
                     longest_palindrome = s[i:j]
        return longest_palindrome

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        longest_palindrome = ''
        
        # fill in diagonal entries
        for i in range(n):
            dp[i][i] = True
            longest_palindrome = s[i]
            
        # fill in remaining entries
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    if j-i == 1 or dp[i+1][j-1]:
                        dp[i][j] = True
                        if j-i+1 > len(longest_palindrome):
                            longest_palindrome = s[i:j+1]
        
        return longest_palindrome