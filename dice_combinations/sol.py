n = int(input())
mod = 10**9 + 7

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    for j in range(1, 7):
        if i - j >= 0:
            dp[i] = (dp[i] + dp[i - j]) % mod

print(dp[n])
