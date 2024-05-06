from functools import lru_cache


def word_break_lru_cache(s: str, wordDict) -> bool:
    @lru_cache(None)
    def helper(s):
        if s == '':
            return True
        for w in wordDict:
            lw = len(w)
            if w == s[:lw]:
                if helper(s[lw:]):
                    return True
        return False
    return helper(s)


print(word_break_lru_cache("applepenapple", ["apple","pen"]))


def word_break_dp(s: str, wordDict) -> bool:
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    max_len = max(map(len, wordDict))

    for i in range(1, n + 1):
        for j in range(i - 1, max(i - max_len - 1, -1), -1): # Only consider words that could fit
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break

    return dp[n]


print(word_break_dp("applepenapple", ["apple","pen"]))